#!/usr/bin/env python3
# -*-coding:utf-8-*-

import os
import tempfile
import shutil
import yaml
import core.equality

DATA_DIRECTORY = 'data'
PROJECTS_FILE = 'projects.yml'


class Project(yaml.YAMLObject, core.equality.Equality):

    yaml_tag = u'!Project'

    def __init__(self, name, templates):
        self.name = name
        self.templates = templates

    def __repr__(self):
        return "%s(name=%r, templates=%r)" % (
            self.__class__.__name__, self.name, self.templates)


class Projects():

    def __init__(self):
        self._conf_file = os.path.join(DATA_DIRECTORY, PROJECTS_FILE)

        if not os.path.exists(DATA_DIRECTORY):
            os.makedirs(DATA_DIRECTORY)
        else:
            if os.path.isdir(self._conf_file):
                raise OSError('Error: "{0}" directory already exists.'.format(
                    self._conf_file))

        if not os.path.isfile(self._conf_file):
            with open(self._conf_file, 'w'):
                pass

        with open(self._conf_file) as conf_file:
            content = yaml.load(conf_file)
            self._content = content if content else []

    def add_project(self, name):
        if any(x.name == name for x in self._content):
            return

        self._content.append(Project(name, []))

        prefix = '{0}.yml_'.format(PROJECTS_FILE)
        f = tempfile.NamedTemporaryFile(prefix=prefix, delete=False)
        tmp_fname = f.name
        f.close()

        with open(tmp_fname, 'w') as tmp_file:
            yaml.dump(self._content, tmp_file)

        try:
            shutil.move(tmp_fname, self._conf_file)
        except:
            raise OSError('Error: Cannot move "{0}" file.'.format(tmp_fname))

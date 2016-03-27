#!/usr/bin/env python3
# -*-coding:utf-8-*-

import os
import yaml

DATA_DIRECTORY = 'data'
PROJECTS_FILE = 'projects.yml'


class Project():

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
            self._content = yaml.load(conf_file)

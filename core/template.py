#!/usr/bin/env python3
# -*-coding:utf-8-*-

import re


class Template():

    _tags = []

    def __init__(self, template_file):

        self.template_file = template_file

        with open(self.template_file, 'r') as source:
            p = re.compile('\{([\w]*)\}')
            self._tags = list(set(p.findall(source.read())))

    @property
    def tags(self):
        return self._tags

#!/usr/bin/env python3
# -*-coding:utf-8-*-

"""chargen

Usage:
  chargen.py start project <project>
  chargen.py add template <template_file> into <project>
  chargen.py (-h | --help)
  chargen.py --version

Options:
 -h --help     Show this screen.
 --version     Show version.
"""


from docopt import docopt
import core.projects


def start_project(project_name):
    recent_projects = core.projects.Projects()
    recent_projects.add_project(project_name)


def add_template_into_project(project_name, template_file):
    recent_projects = core.projects.Projects()
    recent_projects.add_template_into_project(project_name, template_file)


def main(args):
    if args['start'] and args['project']:
        start_project(args['<project>'])
    if args['add'] and args['template'] and args['into']:
        add_template_into_project(args['<project>'], args['<template_file>'])


if __name__ == '__main__':
    args = docopt(__doc__, version='chargen 0.0.1')
    main(args)

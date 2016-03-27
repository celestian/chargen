#!/usr/bin/env python3
# -*-coding:utf-8-*-

"""chargen

Usage:
  chargen.py start project <project>
  chargen.py add template <template> into <project>
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


def main(args):
    if args['start'] and args['project']:
        start_project(args['<project>'])


if __name__ == '__main__':
    args = docopt(__doc__, version='chargen 0.0.1')
    main(args)

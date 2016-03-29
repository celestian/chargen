#!/usr/bin/env python3
# -*-coding:utf-8-*-

import pytest
import os
import yaml
import core.projects


def test_init_project_without_directory(tmpdir):
    core.projects.DATA_DIRECTORY = os.path.join(
        str(tmpdir.realpath()), 'test_subdir')
    core.projects.Projects()

    assert os.path.isdir(core.projects.DATA_DIRECTORY)


def test_init_project_with_file_instead_directory(tmpdir):
    core.projects.DATA_DIRECTORY = os.path.join(
        str(tmpdir.realpath()), 'test_subdir')
    with open(core.projects.DATA_DIRECTORY, 'w'):
        pass

    with pytest.raises(OSError):
        core.projects.Projects()


def test_init_project_create_file(tmpdir):
    core.projects.DATA_DIRECTORY = str(tmpdir.realpath())
    core.projects.Projects()
    dir_content = tmpdir.listdir()
    project_file = os.path.join(
        core.projects.DATA_DIRECTORY,
        core.projects.PROJECTS_FILE)

    assert project_file in dir_content


def test_init_project_new(tmpdir):
    core.projects.DATA_DIRECTORY = str(tmpdir.realpath())
    recent_projects = core.projects.Projects()
    recent_projects.add_project('test_project')
    del recent_projects

    test_project = core.projects.Project(name='test_project', templates=[])

    projects_file = os.path.join(
        core.projects.DATA_DIRECTORY,
        core.projects.PROJECTS_FILE)
    with open(projects_file, 'r') as f:
        content = yaml.load(f)

    assert content == [test_project]


def test_init_project_new_some_exist(tmpdir):
    core.projects.DATA_DIRECTORY = str(tmpdir.realpath())
    recent_projects = core.projects.Projects()
    recent_projects.add_project('test_project_A')
    del recent_projects

    recent_projects = core.projects.Projects()
    recent_projects.add_project('test_project_B')
    del recent_projects

    projects_file = os.path.join(
        core.projects.DATA_DIRECTORY,
        core.projects.PROJECTS_FILE)
    with open(projects_file, 'r') as f:
        content = yaml.load(f)

    test_project_A = core.projects.Project(name='test_project_A', templates=[])
    test_project_B = core.projects.Project(name='test_project_B', templates=[])

    assert len(content) == 2
    assert test_project_A in content
    assert test_project_B in content


def test_init_same_project(tmpdir):
    core.projects.DATA_DIRECTORY = str(tmpdir.realpath())
    recent_projects = core.projects.Projects()
    recent_projects.add_project('test_project_A')
    del recent_projects

    recent_projects = core.projects.Projects()
    recent_projects.add_project('test_project_A')
    del recent_projects

    projects_file = os.path.join(
        core.projects.DATA_DIRECTORY,
        core.projects.PROJECTS_FILE)
    with open(projects_file, 'r') as f:
        content = yaml.load(f)

    test_project_A = core.projects.Project(name='test_project_A', templates=[])

    assert len(content) == 1
    assert test_project_A in content


def test_add_template_into_no_existing_project(tmpdir):
    core.projects.DATA_DIRECTORY = str(tmpdir.realpath())
    recent_projects = core.projects.Projects()

    with pytest.raises(IOError):
        recent_projects.add_template_into_project(
            'test_project_A', 'template.md')


def test_add_template_into_project_no_existing_template(tmpdir):
    core.projects.DATA_DIRECTORY = str(tmpdir.realpath())
    recent_projects = core.projects.Projects()
    recent_projects.add_project('test_project_A')

    with pytest.raises(IOError):
        recent_projects.add_template_into_project(
            'test_project_A', 'template.md')


def test_add_template_into_project(tmpdir):
    core.projects.DATA_DIRECTORY = str(tmpdir.realpath())

    template_file = os.path.join(
        core.projects.DATA_DIRECTORY,
        'test_template.md')
    with open(template_file, 'w'):
        pass

    recent_projects = core.projects.Projects()
    recent_projects.add_project('test_project_A')
    recent_projects.add_template_into_project('test_project_A', template_file)
    del recent_projects

    test_project_A = core.projects.Project(
        name='test_project_A', templates=[template_file])

    projects_file = os.path.join(
        core.projects.DATA_DIRECTORY,
        core.projects.PROJECTS_FILE)
    with open(projects_file, 'r') as f:
        content = yaml.load(f)

    assert len(content) == 1
    assert test_project_A in content

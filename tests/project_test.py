#!/usr/bin/env python3
# -*-coding:utf-8-*-

import pytest
import os
import core.project


def test_init_project_without_directory(tmpdir):
    core.project.DATA_DIRECTORY = os.path.join(
        str(tmpdir.realpath()), 'test_subdir')
    core.project.Project()
    assert os.path.isdir(core.project.DATA_DIRECTORY)


def test_init_project_with_file_instead_directory(tmpdir):
    core.project.DATA_DIRECTORY = os.path.join(
        str(tmpdir.realpath()), 'test_subdir')
    with open(core.project.DATA_DIRECTORY, 'w'):
        pass
    with pytest.raises(OSError):
        core.project.Project()


def test_init_project(tmpdir):
    core.project.DATA_DIRECTORY = str(tmpdir.realpath())
    core.project.Project()
    dir_content = tmpdir.listdir()

    project_file = os.path.join(
        core.project.DATA_DIRECTORY,
        core.project.PROJECTS_FILE)

    assert project_file in dir_content

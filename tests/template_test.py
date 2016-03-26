#!/usr/bin/env python3
# -*-coding:utf-8-*-

import os
import core.template


content = """
Character sheet
===============

Name: {name}

Name again: {name}

Age: {age}
"""


def test_get_tags(tmpdir):

    template_file = os.path.join(str(tmpdir.realpath()), 'test_template.md')
    with open(template_file, 'w') as out:
        out.write(content)

    template = core.template.Template(template_file)
    tags = template.tags

    assert 'name' in tags
    assert 'age' in tags
    assert len(tags) == 2

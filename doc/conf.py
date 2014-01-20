# -*- coding: utf-8 -*-
""" Sphinx config """
import sys
import os
import sphinx_rtd_theme
# pylint: disable=C0103
docs_basepath = os.path.abspath(os.path.dirname(__file__))

addtl_paths = (
    os.pardir,
)

for path in addtl_paths:
    sys.path.insert(0, os.path.abspath(os.path.join(docs_basepath, path)))

from pypicloud_version import git_version_data

extensions = ['sphinx.ext.autodoc', 'numpydoc', 'sphinx.ext.intersphinx',
              'sphinx.ext.linkcode', 'sphinx.ext.autosummary']

master_doc = 'index'
project = u'pypicloud'
copyright = u'2013, Steven Arcangeli'

version_data = git_version_data()
version = version_data['tag']
release = version_data['version']

exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
numpydoc_show_class_members = False
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
}


def linkcode_resolve(domain, info):
    """ Link source code to github """
    if domain != 'py' or not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return "https://github.com/mathcamp/pypicloud/blob/%s/%s.py" % (version_data['ref'], filename)
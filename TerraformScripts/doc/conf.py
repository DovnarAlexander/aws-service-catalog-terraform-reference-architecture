# -*- coding: utf-8 -*-
from __future__ import print_function

from datetime import datetime
import os
import shutil


version = '1.2'
project = u'TerraformScripts'

# If you use autosummary, this ensures that any stale autogenerated files are
# cleaned up first.
if os.path.exists('_autosummary'):
    print("cleaning up stale autogenerated files...")
    shutil.rmtree('_autosummary')

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.autosummary',
              'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = '.rst' # The suffix of source filenames.
master_doc = 'index' # The master toctree document.

copyright = u'%s, Amazon.com' % datetime.now().year

# The full version, including alpha/beta/rc tags.
release = version

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build', '_templates']

pygments_style = 'sphinx'

autoclass_content = "both"
autodoc_default_flags = ['show-inheritance','members','undoc-members']
autodoc_member_order = 'bysource'

html_theme = 'haiku'
html_static_path = ['_static']
htmlhelp_basename = '%sdoc' % project

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

# autosummary
autosummary_generate = True

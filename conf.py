"""
Configuration file for the Sphinx documentation builder.
This file only contains a selection of the most common options. For a full
list see the documentation:
http://www.sphinx-doc.org/en/master/config
"""

# pylint: disable=import-error, invalid-name, redefined-builtin

import datetime as dt
import sphinx_rtd_theme
from sphinx.writers.html import HTMLTranslator

#

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'MIT ORCD User Documentation'
copyright = '%s, MIT Office of Research Computing and Data' % dt.datetime.now().year
author = 'MIT ORCD Project Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
##CNH# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
##CNH# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

##CNH# html_css_files = [
##CNH#     'css/theme_overrides.css',
##CNH# ]

html_js_files = [
  'js/custom.js',
]

html_logo = 'images/orcd-logo.png'

html_context = {
    'vcs_pageview_mode': 'edit',
    'display_github': True,
    'github_user': 'mit-orcd', # Username
    'github_repo': 'orcd-docs-edit', # Repo name
    'github_version': 'main', # Version
    'conf_py_path': '/', # Path in the checkout to the docs root
}

# see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    'canonical_url': 'https://researchcomputing.mit.edu/',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'style_external_links': True,
}


# pylint: disable=too-few-public-methods
class PatchedHTMLTranslator(HTMLTranslator):
    '''HTMLTranslator patched to open external links in new tabs.
    Taken from: 'http://jack.rosenth.al/hacking-docutils.html#sphinx-hacks'
    '''
    def visit_reference(self, node):
        '''Sets link target to '_blank' (new page tab) if link node is
        external to the site.
        '''
        if (node.get('newtab')
                or not (node.get('target')
                        or node.get('internal')
                        or 'refuri' not in node)):
            node['target'] = '_blank'
        super().visit_reference(node)


def setup(app):
    '''Function to setup sphinx customizations.'''
    app.set_translator('html', PatchedHTMLTranslator)


# globally-available substitutions

rst_prolog = r"""
.. |R| replace:: \ :sup:`®`
"""

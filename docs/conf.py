# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# Add several paths so that Sphinx can find documentation locations

import docutils
import os
import sys
import datetime
this_year = str(datetime.datetime.now().year)

sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Pyntel4004-CLI'
copyright = this_year + ', Andrew Shapton'
author = 'Andrew Shapton'

# The full version, including alpha/beta/rc tags
release = 'ENV_VERSION'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    extensions = ["sphinx.ext.autodoc", "sphinx_rtd_theme"]
    html_theme = "alabaster"

else:
    extensions = ["faculty_sphinx_theme", "sphinx.ext.autodoc",
                  "sphinx_rtd_theme"]
    html_theme = "faculty-sphinx-theme"


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_themes_path = ['_themes']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

html_logo = "_static/pyntel4004.svg"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Pygments style for code syntax highlighting
pygments_style = 'sphinx'

# Hide the "Show Source" link
html_show_sourcelink = False

# -- Define custom roles -----------------------------------------------------


def supsub_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Specific role to allow substitutions to be superscripted.
    """
    node = docutils.nodes.superscript()
    node2 = docutils.nodes.substitution_reference(refname=text)
    node += [node2]
    return [node], []


def setup(app):
    """
    Add new role.
    """
    app.add_role('supsub', supsub_role)

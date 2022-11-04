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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PyCon JP'
copyright = '2022, PyCon JP Association'
author = 'PyCon JP Association'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxext.opengraph',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'theme'

html_theme_path = ['_themes']

html_title = 'PyCon JP'

html_last_updated_fmt = '%Y-%m-%d'

html_show_copyright = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_favicon = '_static/favicon.png'

# options for Open Graph
# https://github.com/wpilibsuite/sphinxext-opengraph
ogp_site_url = "https://www.pycon.jp/"
ogp_image = "https://www.pycon.jp/_static/pyconjp_logo.png"
ogp_use_first_image = True

# options for linkcheck
# https://www.sphinx-doc.org/ja/master/usage/configuration.html#options-for-the-linkcheck-builder
linkcheck_ignore = [
    r"https://pyconjp.atlassian.net/.*",
    r"https://drive.google.com/.*",
    r"https://docs.google.com/.*",
    r"http://trac.pycon.jp/.*",
]

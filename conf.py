#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
##source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Marketplace Documentation'
copyright = '2017, CDON AB'
#author = 'CDON AB'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
##version = '0.1'
# The full version, including alpha/beta/rc tags.
##release = '0.1'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '.git', '.gitignore']

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
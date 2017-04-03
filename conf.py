#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Marketplace Documentation'
copyright = '2017, CDON AB'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**/.git', '.gitignore']

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
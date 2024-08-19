from django.core.wsgi import get_wsgi_application

import os.path
import sys
sys.path.append(os.path.abspath("../../"))  # в начале файла
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'final_prom_project'
copyright = '2024, Stanislaw'
author = 'Stanislaw'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']



os.environ['DJANGO_SETTINGS_MODULE'] = 'final_prom_project.settings'

application = get_wsgi_application()
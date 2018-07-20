# -*- coding: utf-8 -*-
import sys, os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.imgmath', 'sphinx.ext.ifconfig', 'sensio.sphinx.configurationblock']
source_suffix = '.rst'
master_doc = 'index'
project = 'Documentation for Research Projects Portal'
copyright = u'2017-2020, SRHU'
version = '0.1'
release = '0.1'
exclude_patterns = ['_includes/*.rst','_developement/*.*','_production/*.*','_test/*.*',]
html_theme = 'sylius_rtd_theme'
html_theme_path = ["_themes"]
htmlhelp_basename = 'Syliusdoc'
man_pages = [
    ('index', 'sylius', u'Research projects Portal Documentation',
     [u'Mayank Dhasmana'], 1)
]

sys.path.append(os.path.abspath('_exts'))
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
rst_epilog = """
"""

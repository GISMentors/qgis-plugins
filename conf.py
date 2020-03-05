# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.join('..', 'sphinx-template'))
from utils import get_month_year, get_year

# -- General configuration ------------------------------------------------

# General information about the project.
project = u'Developing QGIS Plugins'
copyright = u'2018-%d GISMentors' % get_year()

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.9'
# The full version, including alpha/beta/rc tags.
release = '%sbeta' % version

# -- Options for HTML output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'skoleni-qgis-plugins'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', '%s-%s.tex' % (htmlhelp_basename, version), project,
     u'GISMentors', u'manual'),
    ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', htmlhelp_basename, project,
     [copyright], 1)
    ]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', htmlhelp_basename, project,
     copyright, htmlhelp_basename, project,
     'Miscellaneous'),
    ]

html_favicon = "images/favicon.ico"

sys.path.append(os.path.join('..', 'sphinx-template'))

from conf_base import *

todo_include_todos = True
html_use_index = True

local = os.path.abspath(os.path.curdir)
language="en"

rst_prolog += """
.. |pluginBuilderIcon| image:: /{local}/images/icon/plugin_builder.png
   :width: 1.5em

.. |pluginReloaderIcon| image:: /{local}/images/icon/reload.png
   :width: 1.5em

""".format(local=local)


rst_prolog += """
.. |new_plugin| image:: ./src/fiberplanitconvert-01-init/icon.png
   :width: 1.5em
.. |new_plugin1| image:: ../src/fiberplanitconvert-01-init/icon.png
   :width: 1.5em
"""

extlinks["pyqgis"] = ('https://qgis.org/pyqgis/master/core/%s.html', '')
extlinks["pyqt"] = ('https://doc.qt.io/qtforpython/PySide2/QtWidgets/%s.html', '')
extlinks["qt5"] = ('https://doc.qt.io/qt-5/{}.html'.format("%s".lower()), '')

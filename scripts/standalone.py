#!/usr/bin/env python3

# Minimalistic script, that initializes and prepares QGIS libraries
# for use

from qgis.core import *

# But first, we have to setup a correct path to QGIS
QgsApplication.setPrefixPath("/usr/local/", True)

# Next, we create QGIS instance. Second argument will specify,
# if we are creating app with graphical interface or not.
qgs = QgsApplication([], False)

# loading data sources
qgs.initQgis()

#
# Here comes your code for app built on QGIS libraries.
#

# At the end of your program, you need to write exitQgis(). This command will deregister
# data sources, providers and erase layers from computer memory.
qgs.exitQgis()

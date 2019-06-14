######################
Fiber convertor plugin
######################

Goal is to create QGIS plugin which will create layer *Demand Points*
from input CSV data.


===========
User Inputs
===========

1. existing vector layer
2. attribute mapping file
3. target data structure
4. new name for out Esri Shapefile

=======
Process
=======

1. open existing vector file
2. create new Esri Shapefile with given name and based on schema
   according to target data structure
3. add new features to output file with attributes based on input vector file


============
Mapping file
============

Mapping file will be simple CSV file with two columns. First column
contains attributes of the input vector file, second column coresponds
to attributes of the *Demand Points* file:

.. literalinclude:: ../src/fiberplanitconvert/mapping/csv2demanded_points.txt

=====================
Target data structure
=====================

Target file schema contains always:

#. Geometry type (Point)
#. Properties - their names and data types

.. literalinclude:: ../src/fiberplanitconvert-02-qgis-memorylayer/fiberplan/__init__.py
        :lines: 8-31

====================
Development workflow
====================

.. toctree::
        :maxdepth: 1

        01-initial
        02-memorylayer
        03-shapefile
        04-projection
        05-fiona

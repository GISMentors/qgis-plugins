***********************************
Setting coordinate reference system
***********************************

.. note:: The code can be downloaded from https://github.com/GISMentors/yungo-plugins/tree/master/src/fiberplanitconvert-04-qgis-shp-proj

When loading a new layer into project the coordinate reference system
of the layer must be defined. Otherwise a dialog for picking the correct
coordinate reference system appears.

To fix this, we will set the coordinate reference system of the new
created layer according to the input data file.

We are creating two layers:

1. First layer is the memory layer, which is just used for simplicity of the
   manipulation with new features
2. Second layer is a target output Shapefile

Both of them are created slightly in different way, but the both can
have information about coordinate reference system assigned.

============
Memory layer
============

The memory layer is partly created by the URI :pyqgis:`QgsDatasSourceUri`. We
just need to add::

    crs=epsg:NUMBER

To the URI

=========
Shapefile
=========

Shapefile is created using ``QgsVectorFileWriter.writeAsVectorFormat()``
function, which can have :pyqgis:`QgsCoordinateReferenceSystem` type as the 4th
parameter.

Coordinate reference system of the input data can be obtained by ``layer.crs()``

EPSG code can be obtained by using `crs.authid()`.

.. code-block:: python

    >>> crs = QgsCoordinateReferenceSystem.fromEpsgId(4326)
    >>> crs.authid()
    EPSG:4326
    >>> crs.toWkt()
    'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,
    AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,
    AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY
    ["EPSG","9122"]],AUTHORITY["EPSG","4326"]]'

.. task:: Set coordinate reference system for memory layer as well as for a new
    Shapefile.

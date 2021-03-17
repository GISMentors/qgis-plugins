========================================================
Creating custom applications built on QGIS libraries
========================================================

It is usually better to run processes automatically than manually. On
our course(s), we are trying to promote this approach. While working
with geospatial data using `Fiona
<https://fiona.readthedocs.io/en/stable/>`__, `RasterIO
<https://rasterio.readthedocs.io/en/latest/>`__ or `GDAL
<https://pcjericks.github.io/py-gdalogr-cookbook/>`__ libraries, it is
no surprise that we can also use directly QGIS libraries.

Base module is ``qgis.core``, which is required by various tasks that
process data. With QGIS libraries, you can also create your own
application with graphical user interface. This can be achieved by
using module ``qgis.gui``, which enables many interesting options such
as *map canvas*, which we can use to display maps and so on.

Base structure of project
------------------------

Before we start using QGIS libraries, we need to set up some settings
for the start and the end of our script.


.. literalinclude:: ../scripts/standalone.py
   :language: python
   :linenos:

After setting up permissions to *launch file* ``chmod 755
standalone.py`` (Linux) we can safely launch it and leave it running.

.. note:: It is possible that you will need to set up correct
   environmental variable :envvar:`PYTHONPATH` with path to Python
   libraries for QGIS.

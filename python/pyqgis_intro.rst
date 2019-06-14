PyQGIS introduction
===================

Built-in QGIS Python programming-related tools:

#. Python console
#. Built-in Python editor

First steps
-----------

Layers access
^^^^^^^^^^^^^

.. task::
   * list of layers determined from current project (even unsaved) on line :lcode:`1`
   * print layer name and feature count for vector layers (:lcode:`3`)
   * for other layer types print only name (:lcode:`5`)

.. literalinclude:: ./_static/scripts/pyqgis_layers_access_0.py
   :language: python
   :linenos:
   :emphasize-lines: 1, 3, 5

Script to `download <./_static/scripts/pyqgis_layers_access_0.py>`__.

.. figure:: images/qgis_editor.png
   :class: middle

   Example of running simple script from QGIS built-in editor.

.. task::   
   * skip disabled layers on line :lcode:`2`
   * process only vector layers with multipolygon geometry type (:lcode:`5`)
   * loop over features on line :lcode:`9`
   * get feature geometry on line :lcode:`10`
   * get attribute value ``nazev`` (name in Czech) if exists (:lcode:`12`)
   * print feature info (fid, name, area in hectares - assuming map units
     meters), see line :lcode:`16`
  
  
.. literalinclude:: ./_static/scripts/pyqgis_layers_access_1.py
   :language: python
   :linenos:
   :emphasize-lines: 2, 5, 9, 10, 12, 16
                     
Script to `download <./_static/scripts/pyqgis_layers_access_1.py>`__.

Vector data, features access and editing
----------------------------------------

Sample data (ice cream shops in Czech Republic downloaded from
OpenStreetMap as points only): `ice_cream.csv <./_static/data/ice_cream.csv>`__.

Adding CSV-based layers
^^^^^^^^^^^^^^^^^^^^^^^

.. task::
   * load layer without geometry (as table) (see lines :lcode:`2` and :lcode:`5`)
   * add table layer into layer tree (:lcode:`6`)

.. literalinclude:: ./_static/scripts/pyqgis_csv_layer_0.py
   :language: python
   :linenos:
   :emphasize-lines: 2, 5, 7
     
Script to `download <./_static/scripts/pyqgis_csv_layer_0.py>`__.

.. task::
   * geometry built from longitute and latitude
   * set spatial reference system to :epsg:`4326`
   * add map layer into layer tree

.. literalinclude:: ./_static/scripts/pyqgis_csv_layer_1.py
   :language: python
   :linenos:
   :emphasize-lines: 2

Script to `download <./_static/scripts/pyqgis_csv_layer_1.py>`__.

Save layer into file-based GIS format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. task::
   * reproject to S-JTSK (:epsg:`5514`) (target CRS set on line :lcode:`4`)
   * save layer into Esri Shapefile format (this task performed on
     lines :lcode:`5-7`)

.. literalinclude:: ./_static/scripts/pyqgis_save_0.py
   :language: python
   :linenos:
   :emphasize-lines: 1, 4, 5-7

Script to `download <./_static/scripts/pyqgis_save_0.py>`__.

.. task:: Improvements

   * check if input layer found (see line :lcode:`1`)
   * check for writter's errors (see `cookbook example <https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html#from-an-instance-of-qgsvectorfilewriter>`__)

Editing vector features
^^^^^^^^^^^^^^^^^^^^^^^

.. task::
   * select features in distance of 1km from current position (`14.3881100E, 50.1041200N <https://www.openstreetmap.org/way/99013221>`__), see lines :lcode:`8` and :lcode:`21`
    * point of interest must be transformed into layer's CRS (:lcode:`10-13`)
    * area of interest is defined by rect on lines :lcode:`15-19`
   * invert selection on line :lcode:`24`
   * delete selected features on line :lcode:`27`
    * note that layer must be switched to edinging mode, it can be
      done eg. by triggers, see lines :lcode:`26,28`

.. literalinclude:: ./_static/scripts/pyqgis_editing_0.py
   :language: python
   :linenos:
   :emphasize-lines: 8, 10-13, 15-19, 21, 24, 26-28
		     
Script to `download <./_static/scripts/pyqgis_editing_0.py>`__.

.. task:: Compare with

   .. code-block:: python

      layer.startEditing()
      layer.deleteSelectedFeatures()
      layer.commitChanges()

******************
Publish the plugin
******************

Let's imagine that we are satisfied with our plugin and we would like
to share it with our colleagues or other QGIS users. There are several
steps which must be performed.

Create zip package
==================

A zip package can be created by :program:``pb_tool`` (see
:doc:`build_plugin`). Go to your plugin directory and type:

.. code-block:: bash

   pb_tool zip

A new zip file will be created in the current directory. This archive
contains all necessary information in order to install the QGIS
plugin.

.. tip:: Try to install QGIS plugin directly from this zip file. Go to
         :menuselection:`Plugins --> Manage and Install
         Plugins...`. Choose `Install from ZIP`.

.. task:: Improve plugins metadata

   Modify :file:`metadata.txt` file.

Official QGIS plugin repository
===============================

You can publish your plugin in `official QGIS Plugin repository
<https://plugins.qgis.org/plugins/>`__. Plugin must fulfill basic
requirements (GNU GPL license, documentation included). You can upload
the plugin at
https://plugins.qgis.org/accounts/login/?next=/plugins/add/. Note that
it can take few days when your plugin will be approved by the
moderators.

Local QGIS plugin repository
============================

It can be relatively easy to set up a local (in-house) QGIS plugin
repository. It is only question of creating a XML file accessible via
HTTP protocol (so web server must run in your infrastructure).

Simple example for our plugin:

.. code-block:: xml

   <?xml version="1.0"?>
   <plugins>
    <pyqgis_plugin name="fiberplanitconvert" version="0.1">
        <description>Convert input files to output FiberPlanIT shapefiles</description>
        <homepage>https://ctu-geoforall-lab.github.io/qgis-vfk-plugin/</homepage>
        <qgis_minimum_version>3.4</qgis_minimum_version>
        <file_name>fiberplanitconvert.zip</file_name>
        <author_name>GISMentors</author_name>
        <download_url>http://server/fiberplanitconvert.zip</download_url>
    </pyqgis_plugin>
   </plugins>

Store it as :file:`qgis_plugins.xml` and check if the file is
accessible over HTTP protocol, eg. http://server/qgis_plugins.xml.

Now add the new repository to QGIS. Go to :menuselection:`Plugins -->
Manage and Install Plugins...`. 

.. figure:: ./images/new_repository.png

   In tab ``Settings`` add the new repository.

Now you should see the plugin in the search list.

.. figure:: ./images/local_repo_new_plugin.png

.. tip:: When searching for more advanced solutions take a look at
         https://github.com/boundlessgeo/qgis-plugin-repos/tree/master/docker-plugins-xml
         or similar solutions.

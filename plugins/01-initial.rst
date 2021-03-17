*********************
Plugin initialization
*********************

===================
Create QGIS project
===================

Use :menuselection:`Layer --> Add layer --> Add vector layer`, icon
|mActionAddOgrLayer| :sup:`Add vector layer` or
:kbd:`Ctrl+Shift+V`. Add multiple layers to your new QGIS project.

   .. _np-project:

   .. figure:: ../images/qgis-project.png
      :class: middle

      Sample QGIS project.

===============
Activate plugin
===============

In :menuselection:`Plugins --> Manage and install plugins` search and
activate the `Save Views` plugin.

.. figure:: ../images/save-views-enable.png
   :class: middle
           
   Activate the plugin.

See a new icon in the toolbar |new_plugin1|. Plugin can be open.

.. figure:: ../images/plugin-ui-template.png

   Empty plugin dialogue.

===========
Qt Designer
===========

Start the `Qt Desginer tool
<https://doc.qt.io/qt-5/qtdesigner-manual.html>`__ and open the
:file:`save_views_dockwidget_base.ui` file.

.. figure:: ../images/qt_designer_01.png
   :class: middle
           
   The dialogue is empty so far.

========
The code
========

The key file is :file:`save_views.py` and the ``run()`` method:

.. literalinclude:: ../src/save_views01-init/save_views.py
        :lines: 211-232
        :linenos:

.. note:: The code can be downloaded from `our Github
          <https://github.com/GISMentors/qgis-plugins/tree/master/src/save_views-01-init>`__.

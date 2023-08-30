=================================
Launching code on startup of QGIS
=================================

In this section we will describe how to launch specific Python code
when QGIS is starting. It can configured it by using
:envvar:`PYQGIS_STARTUP` or by creating a Python script in home
directory for QGIS.  This folder is usually located in:

* On Linux :file:`.local/share/QGIS/QGIS3/`
* On Windows: :file:`AppData\Roaming\QGIS\QGIS3\profiles\default\python`
* On macOS: `Library/Application Support/QGIS/QGIS3/profiles/default`

After you locate the correct directory, create a file called :file:`startup.py`.
This script will be run automatically on startup. 

.. note:: As you can see above, path to this directory is different on
   every operation system. To locate it correctly, open
   :menuselection:`Plugins --> Python console` and type
   :code:`QStandardPaths.standardLocations(QStandardPaths.AppDataLocation)`
   By such statement also presence of required modules can be
   checked.

.. literalinclude:: ../scripts/startup.py

Thanks to that, our required modules (like `fiona`) and working
environment are set up and ready to use.

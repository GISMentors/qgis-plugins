=================================
Launching code on startup of QGIS
=================================

If we launch some program while starting QGIS, some code may be executed.
We can configure it by using :envvar:`PYQGIS_STARTUP`
or by creating a script in Python home directory for QGIS.
This forlder is usually located in:

* On Linux `.local/share/QGIS/QGIS3/`
* On Windows: `AppDataRoamingQGISQGIS3profilesdefault/python`
* On macOS: `Library/Application Support/QGIS/QGIS3/profiles/default`

After you locate the correct directory, create a :file:`startup.py`.
This script will run automatically on startup. 

.. note:: As you can see above, path to this directory is different on every operation system. 
	To locate it correctly, open:
        :menuselection:`Plugins --> Python console` and type this code:
 `QStandardPaths.standardLocations(QStandardPaths.AppDataLocation)`
This code should show you default path to that directory.
We can also enhance it and insert more parameters. 
We can not only locate desired directory, but also check presence of required modules.

.. literalinclude:: ../scripts/startup.py

Script is then executed on QGIS startup. Thanks to that, our required modules and working environment are set up and ready to use.

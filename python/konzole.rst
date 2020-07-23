.. |clearConsole| image:: ../images/icon/iconClearConsole.png
   :width: 1.5em
.. |classConsole| image:: ../images/icon/iconClassConsole.png
   :width: 1.5em
.. |runConsole| image:: ../images/icon/iconRunConsole.png
   :width: 1.5em
.. |showEditorConsole| image:: ../images/icon/iconShowEditorConsole.png
   :width: 1.5em
.. |settingsConsole| image:: ../images/icon/iconSettingsConsole.png
   :width: 1.5em
.. |helpConsole| image:: ../images/icon/iconHelpConsole.png
   :width: 1.5em

====================
Interactive console
====================

Whether you use MS Windows or Linux, you should have `QGIS
<http://training.gismentors.eu/qgis-zacatecnik/instalace/index.html>`_  installed with Python console. We will use it now to determine system version.

:menuselection:`Plugins --> Python console` (:kbd:`Ctrl+Alt+P`). This should open a new window with interactive console.

.. figure:: images/console.png

    Starting Python console


After you open Python console, you should see these buttons:

|clearConsole|
    Clears window contents and deletes all displayed text
|runConsole|
    Run command. You can use this button or just simply press
    :kbd:`Enter`
|showEditorConsole|
    Launches a text editor. You can edit your code through it
|settingsConsole|
    Advanced settings of console and editor
|helpConsole|
    This will launch web browser with help manual

.. todo:: Description |classConsole| - valid only for 3.0.2/master

Python console gives us option to write code more interactively. 
It automatically changes colors for different types of syntax. 
You can also save your code to external file and it shows quick helping tips.
When you press :kbd:`Ctrl-Alt-Space`, it will automatically insert commands.
To see history of commands, press :kbd:`Ctrl-Shift-Space`. 

Typing a command:

.. code-block:: python

    >>> _pyqgis

Will display documentation for Python in QGIS as a new tab in web browser.

.. code-block:: python

    >>> _api

This command will also display documentation, but just for Python.

Editor
------

Built-in code editor can be turned on by clicking on icon |showEditorConsole|.
Automatic fill in function (:kbd:`Ctrl+Space`) can be very useful while writing a code.
To check code syntax, press (:kbd:`Ctrl+4`).
Another useful functions are search in code and inspect code.

.. figure:: images/editor.png

    Built-in code editor

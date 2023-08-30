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

Whether you use MS Windows or Linux, you should have QGIS installed
with Python console. We will use it now to determine system version.

Go to :menuselection:`Plugins --> Python console`
(:kbd:`Ctrl+Alt+P`). This should open a new window with an interactive
console.

.. figure:: images/console.png
   :class: middle
           
   Interactive Python console in QGIS.

After you open Python console, you should see these buttons:

|clearConsole|
    Clear window contents and delete all displayed text
|runConsole|
    Run command. You can use this button or just simply press
    :kbd:`Enter`
|showEditorConsole|
    Opens a text editor. You can edit your code through it
|settingsConsole|
    Advanced settings of console and editor
|helpConsole|
    This will launch web browser with help manual

Python console gives us option to write code more
interactively. Moreover the console supports syntax highlight. You can
also save your code to a file.  When you press :kbd:`Ctrl-Alt-Space`,
it will automatically insert commands.  To see history of commands,
press :kbd:`Ctrl-Shift-Space`.

Let's start with a command:

.. code-block:: python

    >>> _pyqgis

which display documentation for Python in QGIS as a new tab in web browser.

Similarly

.. code-block:: python

    >>> _api

will also display C++ API documentation.

.. _buildin-editor:

Editor
------

Built-in code editor can be open by clicking on icon
|showEditorConsole|. Automatic prompting (:kbd:`Ctrl+Space`) can be
very useful while writing a code. To check code syntax, press
(:kbd:`Ctrl+4`). Another useful functions are search in code and
inspect the code.

.. figure:: images/editor.png
   :class: middle
           
   Built-in Python code editor.

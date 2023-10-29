############################
Installation and environment
############################

For every development, some system tweaks and necessary tools are needed. 

***********
Text Editor
***********

You can use any text editor, which you are already using for your
daily programming activities. Even :ref:`build-in QGIS editor
<buildin-editor>` can be fine. If you are in doubt, which one to
choose, consider one of following editors:

* `Sublime <https://www.sublimetext.com/>`__ A sophisticated text
  editor for code, markup and prose
* `Visual Studio Code <https://code.visualstudio.com/>`__ A
  lightweight but powerful source code editor which runs on your
  desktop and is available for Windows, macOS and Linux.
* `PyCharm <https://www.jetbrains.com/pycharm/>`_ The Python IDE for
  Professional Developers
* `add your own`...

Sublime is rather simplier editors (with complex features in
the backend though), while Visual Studio Code and PyCharm are more
Integrated development enviroments.

It is worth to spend some time with some tutorial of your featured editor to
know all the features and hidden gems, to become more effective.

.. _qtdesigner:

***********
Qt Designer
***********

`Qt Designer <https://www.qt.io/design>`__ is a tool for creating
destkop applications, which will be later empowered with some
programming code to make the graphical user interface work.

Usually, the application design is created by the programmer, but it does no
need to be the case, since one does not have to know any programming in order to
create user interface. You just have to understand principals of the UX design -
therefore the look and feel of the application can be done by someone else as
well as the final programming code, which will bring the apparence of the
application to life.

Install Qt Designer on Linux
============================

On Linux, you should be able to use your favourite packaging tool, like
:program:`apt`

.. code-block:: bash

   sudo apt install python3-pyqt5 libqt5designer5
        
Install Qt Designer on Windows
==============================

On MS Windows platform QT Designer is installed together with QGIS. In
any case you can install it using OSGeo4W installator, choose
``Advanced installation`` and search for the ``qt5-tools`` package.

.. figure:: images/install-qt5-tools.png
   :class: middle

.. figure:: images/qt-designer-windows-start.png
   :class: small
           
   Qt Designer can be found in the start menu of Windows.

====================================
Calling processing tools from Python
====================================

See `QGIS documentation
<https://docs.qgis.org/3.28/en/docs/user_manual/processing/console.html>`__
for details.

QGIS processing is available in Python through ``processing``
module. On line :lcode:`3` we will loop over all available
algorithms. By a simple condition on line :lcode:`4` only tools
containing a word "buffer" in the name will be printed out.

.. literalinclude:: ../_static/scripts/processing_search.py
   :language: python
   :linenos:
   :lines: 1-5
   :emphasize-lines: 1, 3, 4

List parameters for selected algorithm:

.. literalinclude:: ../_static/scripts/processing_search.py
   :language: python
   :linenos:
   :lines: 7-9
   :emphasize-lines: 2
                     
Let's select `native:buffer
<https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#qgisbuffer>`__
tool and execute it by Python code.

.. literalinclude:: ../_static/scripts/processing_buffer.py
   :language: python
   :lines: 1-10
   :linenos:
   :emphasize-lines: 4

Newly created layer can be added into layer tree (see next section for :doc:`pyqgis_intro`):

.. literalinclude:: ../_static/scripts/processing_buffer.py
   :language: python
   :lines: 12-13
   :linenos:                     

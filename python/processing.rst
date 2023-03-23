====================================
Calling processing tools from Python
====================================

See `QGIS documentation
<https://docs.qgis.org/3.22/en/docs/user_manual/processing/console.html>`__
for details.

QGIS processing is available in Python through ``processing``
module. On line :lcode:`3` we will loop over all available
algorithms. By a simple condition on line :lcode:`5` only tools
containing a word "buffer" in the name will be printed out.

.. literalinclude:: ../_static/scripts/processing_search.py
   :language: python
   :linenos:
   :emphasize-lines: 1, 3, 5

Let's select `native:buffer
<https://docs.qgis.org/3.22/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#qgisbuffer>`__
tool and execute it by Python code.

.. literalinclude:: ../_static/scripts/processing_buffer.py
   :language: python
   :linenos:
   :emphasize-lines: 3

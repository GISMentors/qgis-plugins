========================================================
Tvorba vlastních aplikací postavených na knihovnách QGIS
========================================================

Některé procesy je výhodné vykonávat automatizovaně, místo množství ruční práce.
Na našich kurzech se snažíme tento přístup propagovat a nebude překvapením, že
je možné vedle nástrojů pro práci s prostorovými daty typu `Fiona`_,
`RasterIO`_ nebo `GDAL`_, můžeme využít i knihovny QGIS.

Základem je modul `qgis.core`, který je potřeba pro většinu úkolů spojených se
zpracováním dat. Ale pomocí knihoven QGIS lze také celkem jednoduše vytvořit
vlastní aplikaci s kompletním grafickým rozhraním, a to pomocí modulu
`qgis.gui`, který zpřístupňuje různá části grafického rozhraní, jako je
*canvas* pro vykreslení mapy, ale i další.

Základní kostra projektu
------------------------

Pro to, aby šlo využít knihovny QGIS, je potřeba trochu režie při inicializaci
projektu i při jeho ukončení:


.. literalinclude:: ../scripts/standalone.py
   :language: python
   :linenos:

Po nastavení práv pro *spuštění souboru* `chmod 755 standalone.py` můžeme
program spustit a nechat proběhnout.

.. note:: Pravděpodobně bude potřeba ještě nastavit správnou proměnnou
    :envvar:`PYTHONPATH` s cestou k instalaci QGIS knihoven pro Python.

.. _fiona: https://fiona.readthedocs.io/en/stable/
.. _rasterio:  https://rasterio.readthedocs.io/en/latest/
.. _gdal: https://pcjericks.github.io/py-gdalogr-cookbook/

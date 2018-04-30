***********
První kroky
***********

V této kapitole si projdeme prví kroky, abychom se seznámili se systémem a
prostředím, ve kterém budeme vyvýjet. Předpokládáme, že máte `základní znalost systému QGIS
<http://training.gismentors.eu/qgis-zacatecnik>`_  a `základní
znalost programovacího jazyka Python <https://python.cz/zacatecnici/>`_.

=====
Verze
=====

V tomto školení budeme používat současnou *testing* verzi systému QGIS 3.x a
Python verze 2.7.

Současná verze QGIS podporuje zásuvné moduly pro *Python 2*. Python 2 je ale
již zastaralá verze a měla by se opustit.


.. todo:: Je potřeba vyjasnit, v jaký verzi Pythonu jaká verze QGIS jede. Na mém
        lokále to vypadá na systémový Python 3.6 a QGIS zatím funguje (QGIS 3.0,
        vlastní kompilace).

.. note:: V současnosti (jaro 2018) se nacházíme v přechodové době, kdy QGIS,
        ale i GRASS GIS pracují na přechodu na Python 2.
        V budoucí stabilní verzi QGIS 3.x s dlouhodobou podporou již nebude
        Python 3 problém.

=============
QGIS a Python
=============
Od verze 0.9 programu QGIS lze používat programovací jazyk Python pro přístup k
některým funkcím. Python lze v kombinaci s QGISem používat v následujcích
situacích:

* Automatický skript při startu QGIS
* Použití interkativní konzole a zadávání příkazů napřímo
* Tvorba a použití zásuvných modulů
* Tvorba vlastních aplikací postavených na knihovných QGIS

Dále je možné tvořit zásuvné moduly pro QGIS server. 


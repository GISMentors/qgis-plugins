***************************************
Instalace vývojářských zásuvných modulů
***************************************

Zásuvné moduly QGIS potřebují celou řadu pomocích skriptů a metadat, tak, aby se
zásuvný modul do QGIS správně načetl. Ani zkušení vývojáři nepohrdnou možností,
nechat si vytvořit tato metadata a pomocné soubory automatizovaně. K tomu nám
slouží zásuvný modul QGIS pro tvorbu zásuvných modulů `Plugin builder <https://plugins.qgis.org/plugins/pluginbuilder/>`_.

Když zásuvný modul vyvíjíme postupujeme často iterativně - po menších krocích.
Při každé změně kódu je potřeba námi vyvíjený zásuvný modul znovu načíst do
prostředí QGIS - jinak bychom jej museli při každé změně restartovat. K takovému
opětovnému načtení slouží zásuvný modul `Plugin reloader <https://plugins.qgis.org/plugins/plugin_reloader/>`_.

Tyto dva zásuvné moduly je potřeba mít nainstalované prostřednictvím nástroje 
pro správu zásuvných modulů  :menuselection:`Zásuvné moduly --> Spravovat a
instalovat zásuvné moduly...` ikona |mActionShowPluginManager|.

.. note:: Postupujte podle návodu z `kurzu pro začátečníky <http://training.gismentors.eu/qgis-zacatecnik/ruzne/qgis_pluginy.html>`_. P
        Pro instalaci je potřeba mít povoleny :guilabel:`Experimentální` zásuvné moduly.

Na liště nástrojů v QGIS nám přibudou dvě ikonky pro oba zásuvné moduly: ikona
|pluginBuilderIcon| a |pluginReloaderIcon|.

Instalace nástroje pb_tool
==========================

Nástroj `pb_tool <http://g-sherman.github.io/plugin_build_tool/>`_ pro
příkazovou řádku slouží pro jednodušší práci při vývoji zásuvného modulu.
`pb_tool` umí například

* Kompilovat zdrojové soubory pro uživatelské rozhraní
* Uložit vyvíjený zásuvný modul do cílového adresáře pro QGIS
* Vytvořit ZIP soubor s pluginem pro uložení do repozitáře
* Vyčistit dočasné soubory
* Pomoci s překladem

a další.

Nástroj nainstalujeme v příkazové řádce příkazem

.. code-block:: bash

        python3 -m pip install pb_tool

Nebo prostě

.. code-block:: bash
        
        pip3 install pb_tool

Ověříme, že je řádně nainstalovaný příkazem

.. code-block:: bash

        pb_tool

Pokud se nám ukáže nápověda, je vše jak má být.

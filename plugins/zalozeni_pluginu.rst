****************
Založení pluginu
****************

Založení pluginu provedeme nejjednodušeji pomocí pluginu QGIS Plugin Builder,
který spustíme buď z menu :menuselection:`Zásuvné moduly --> Plugin Builder` nebo
pomocí ikony |pluginBuilderIcon| z nástrojové lišty.


.. figure:: ../images/builder_init.png

        Spuštění QGIS Plugin Builder

Vyplníme potřebné hodnoty:

Class name
        Jméno hlavní třídy (pro jazyk Python) (obvykle začíná velkým písmenem a
        slova jsou naznačena také velkým posmenem)

Plugin name
        Jméno zásuvného modulu tak, jak bude viditelný pro uživatele - může
        obsahovat mezery a další znaky

Description
        Krátký popis

Module name
       Jméno modulu - zejména pak adresáře, do kterého bude modul uložený 


.. figure:: ../images/builder_init_values.png

        Vyplnění vstupních hodnot

V dalším kroce je potřeba vyplnit delší popis pluginu a jeho funkce


.. figure:: ../images/builder_about.png

        Nastavení položky `About` zásuvného modulu

V dalším kroku je potřeba nastavit šablonu zásuvného modulu. Na výběr máme ze
tří možností

1. :guilabel:`Tlačítko a dialog` - výchozí nastavení, které vytvoří tlačítko na liště QGIS a
   po jeho kliknutí se vykreslí vstupní dialogové okno pro zadání dalších hodnot
2. :guilabel:`Tlačítko a dock` - po aktivaci modulu se vykreslí dokovatelné
   okno, které lze začlenit do grafickéhé rozhranní QGIS (podobně jako přepínač
   vrstev, nástroj dotazování nebo třeba konzole Python).
3. Poskytovatel Processing nástrojů - speciální případ zásuvného modulu, který
   může být spouštěn jako další z komponent Processing zásuvného modulu.

Další volbou je pak možnost začlenit zásuvný modul do kterého z menu, výchozí je
:guilabel:`Pluginss` ale na výběr máme :guilabel:`Raster` :guilabel:`Vector` a
další.


.. figure:: ../images/builder_template.png

        Volba šablony zásuvného modulu

V dalším kroku nám Plugin Builder nabízí tvorbu některých souborů s metadaty. V
tuto chvíli necháme zaškrtnuté všechny metasoubory.

.. figure:: ../images/builder_meta.png

        Volba vytvořených metadat k zásuvným modulům.

Jednotlivé soubory slouží k pozdějšímu nastavení

Internationalization
        Překlad zásuvného modulu do více jazyků
Help
        Nápověda pro zásuvný modul
Unit tests
        Testy pro modul
Helper scripts
        Pomocné skripty pro publikaci zásuvného modulu v repozitáři
        http://plugins.qgis.org a pro překlad a testování.
Makefile
        Makefile je konfigurační soubor pro automatizovaný build projektů
        prostřednictvím programu `make`.
pb_tool
        Vytvoří konfigurační soubor pro nástroj `pb_tool`, který pomáhá  se
        sestavením zásuvného modulu na různých operačních systémech.

        Doporučujeme používat právě `pb_tool` na místo výše zmíněného `make`

V dalším kroku je potřeba nastavit linky k nástroji pro správu chyb, repozitář
projektu a jeho domovskou stránku. V této fázi projektu zatím nemáme ani jedno,
nicméně je dobrým zvykem tyto linky nastavit a  udržovat aktuální.


.. figure:: ../images/builder_links.png

        Linky vedoucí na repozitář a hlášení chyb pluginu

V posledním kroku zvolíme cílový adresář, kam bude zásuvný  modul uložen.
Není důležité, aby byl uložen do cílového adresáře se zásuvnými moduly - naopak,
uložte jej mezi své další vývojové projekty.

.. figure:: ../images/builder_final.png

        Nastavení cílové cesty nového zásuvného modulu.

Po kliknutí na tlačítko :guilabel:`Generate` je  plugin vytvořen.

.. figure:: ../images/builder_report.png

        Finální report o tvorbě zásuvného modulu

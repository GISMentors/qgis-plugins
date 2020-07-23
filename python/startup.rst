=============================
Spuštění kódu při startu QGIS
=============================

Při spuštění nějakého programu při startu programu QGIS se může vykonat určitý
kód. To nastavíme buď za použití proměnné prostředí :envvar:`PYQGIS_STARTUP`
nebo tím, že vytvoříme skript v domovské složce Pythonu pro QGIS, což je 

* na operačním systému Linux `.local/share/QGIS/QGIS3/`
* na Windows: `AppDataRoamingQGISQGIS3profilesdefault/python`
* na macOS: `Library/Application Support/QGIS/QGIS3/profiles/default`

se jménem :file:`startup.py`. Ten bude automaticky vykonán při spuštění.

.. note:: Výchozí adresář pro umístění souboru `startup.py` se může na každém
        systému měnit. Pro ověření správného umístění otevřete 
        :menuselection:`Zásuvné moduly --> Python konzole` a  po vložení kódu
        `QStandardPaths.standardLocations(QStandardPaths.AppDataLocation)` se
        vám výchozí cesty vypíší.

Do tohoto skriptu můžeme nastavit například proměnné prostředí nebo zkontrolovat
přítomnost potřebných modulů:

.. literalinclude:: ../scripts/startup.py

Skript je vykonán při startu QGIS a veškeré potřebné moduly a nastavení
prostředí by mělo být hotové.

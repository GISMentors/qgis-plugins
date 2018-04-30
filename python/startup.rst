=============================
Spuštění kódu při startu QGIS
=============================

Při spuštění nějakého programu při startu programu QGIS se může vykonat určitý
kód. To nastavíme buď za použití proměnné prostředí :envvar:`PYQGIS_STARTUP`
nebo tím, že vytvoříme skript v domovské složce Pythonu pro QGIS
(:file:`.qgis2/python`) se jménem :file:`startup.py`. Ten bude automaticky
vykonán při spuštění.

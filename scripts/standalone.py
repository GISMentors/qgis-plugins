#!/usr/bin/env python3

# Minimalistický skript, který inicializuje knihovny QGIS a připraví je k
# použití

from qgis.core import *

# Nejprve musíme nastavit cestu k instalaci QGIS
QgsApplication.setPrefixPath("/usr/local/", True)

# vytvoříme instanci aplikace QGIS. Druhý argument nastavuje, jestli se bude
# jednat o aplikaci využívající grafické rozhraní nebo ne
qgs = QgsApplication([], False)

# načtení poskytovatelů dat
qgs.initQgis()

#
# Na toto místo přijde vlastní kód aplikace, využívající knihovnu QGIS
#

# Na konci programu je potřeba zavolat exitQgis(), aby došlo k odregistrovaná
# poskytovatelů dat a vymazání vrstev z paměti počítače
qgs.exitQgis()

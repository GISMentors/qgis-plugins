from qgis.core import *

# Nastaveni instalacni cesty QGIS knihoven, neni to ale nutne, pokud vyuzivate
# beznou instalaci v systemu
# QgsApplication.setPrefixPath("/cesta/k/instalaci/qgis", True)

# vytvorit odkaz na objekt QgsApplication
# druhy argument nastaveny na hodnotu False vypne graficke rozhrani
qgs = QgsApplication([], True)

# nacteni provideru
qgs.initQgis()

# sem prijde vas kod, nacteni vrstev, procesovani, ...

# zavolanim metody exitQgis() se uvolni pamet a program muze byt ciste ukoncen
qgs.exitQgis()

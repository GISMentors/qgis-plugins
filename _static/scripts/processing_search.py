from qgis import processing

for alg in QgsApplication.processingRegistry().algorithms():
    name = alg.displayName()
    print(alg.id(), "->", name)

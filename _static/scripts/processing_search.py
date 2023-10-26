from qgis import processing

for alg in QgsApplication.processingRegistry().algorithms():
    name = alg.displayName()
    if 'buffer' in name:
        print(alg.id(), "->", name)
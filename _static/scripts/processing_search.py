from qgis import processing

for alg in QgsApplication.processingRegistry().algorithms():
    if 'buffer' in alg.id():
        print(alg.id(), "->", alg.displayName())

    if alg.id() == 'native:buffer':
        for p in alg.parameterDefinitions():
            print(p.name(), p.description())

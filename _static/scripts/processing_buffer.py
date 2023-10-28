from qgis import processing

output = '/tmp/pozarni_stanice_10km.shp'
processing.run("native:buffer", {
    'INPUT': '/home/martin/geodata/gismentors/qgis-data/shp/osm/pozarni_stanice.shp',
    'DISTANCE': 10000,
    'SEGMENTS': 10,
    'DISSOLVE': True,
    'OUTPUT': output
})

layer = QgsVectorLayer(output, os.path.basename(output), 'ogr')
QgsProject.instance().addMapLayer(layer)

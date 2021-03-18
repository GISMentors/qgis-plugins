from qgis import processing

processing.run("native:buffer", {
    'INPUT': '/home/martin/geodata/gismentors/qgis-data/shp/osm/pozarni_stanice.shp',
    'DISTANCE': 10000,
    'SEGMENTS': 10,
    'DISSOLVE': True,
    'OUTPUT': '/tmp/pozarni_stanice_10km.shp'
})

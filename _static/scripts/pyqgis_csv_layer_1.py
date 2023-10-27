filename = '/home/martin/Downloads/ice_cream.csv'
uri = 'file:///{}?delimiter=,&xField=lon&yField=lat&crs=epsg:4326'.format(filename)

name = os.path.splitext(os.path.basename(filename))[0]
layer = QgsVectorLayer(uri, name, 'delimitedtext')

QgsProject.instance().addMapLayer(layer)

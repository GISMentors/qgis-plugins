filename = '/home/martin/git/gismentors/yungo-plugins/_static/data/ice_cream.csv'
uri = 'file:///{}?delimiter=,'.format(filename)

name = os.path.splitext(os.path.basename(filename))[0]
layer = QgsVectorLayer(uri, name, 'delimitedtext')

QgsProject.instance().addMapLayer(layer)

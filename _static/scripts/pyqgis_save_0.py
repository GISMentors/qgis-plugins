layer = QgsProject.instance().mapLayersByName('ice_cream')[0]

shp_file = "/tmp/ice_cream.shp"
crs = QgsCoordinateReferenceSystem("EPSG:5514")
QgsVectorFileWriter.writeAsVectorFormat(
    layer, shp_file,
    "UTF-8", driverName="ESRI Shapefile", destCRS=crs)
                                        
layer_shp = QgsVectorLayer(shp_file, "test", "ogr")
print (layer_shp.isValid())
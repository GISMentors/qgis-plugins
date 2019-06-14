shp_file = "/tmp/ice_cream.shp"
layer = QgsVectorLayer(shp_file, "test", "ogr")

QgsProject.instance().addMapLayer(layer)

x = 14.3881100
y = 50.1041200
geom = QgsGeometry.fromPointXY(QgsPointXY(x, y))

p_crs = QgsCoordinateReferenceSystem("EPSG:4326")
trans = QgsCoordinateTransform(
    p_crs, layer.crs(), QgsProject.instance())
geom.transform(trans)

p = geom.asPoint()
offset = 1500
p1 = QgsPointXY(p.x() - offset, p.y() - offset)
p2 = QgsPointXY(p.x() + offset, p.y() + offset)
aoi = QgsRectangle(p1, p2)

layer.selectByRect(aoi)
print (len(layer.selectedFeatures()))

layer.invertSelection()

iface.actionToggleEditing().trigger()
iface.actionDeleteSelected().trigger()
iface.actionToggleEditing().trigger()
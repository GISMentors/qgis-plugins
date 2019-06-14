fields = QgsFields()
fields.append(QgsField("attr1", QVariant.String))
fields.append(QgsField("attr2", QVariant.Int))

file = QgsVectorFileWriter(
        "/tmp/out.shp",
        "UTF8",
        fields,
        QgsWkbTypes.Point,
        QgsCoordinateReferenceSystem(4326),
        "ESRI Shapefile"
    )
    
layer = QgsVectorLayer("/tmp/out.gpkg", "baf", "ogr")
QgsProject.instance().addMapLayer(layer)

feature = QgsFeature()
feature.setFields(layer.fields())


feature.setGeometry(QgsGeometry().fromWkt("Point(0 0)"))
feature.setAttribute("attr1", "attttr")
feature.setAttribute("attr2", 2)

layer.startEditing()
layer.addFeature(feature)
layer.commitChanges()
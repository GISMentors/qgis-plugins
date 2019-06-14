from qgis.core import *

def convert(input_layer, mapping, data_type, layer_name, output_file):
    """Convert input data using QGIS tools
    """

    new_layer = _create_layer(data_type, layer_name, input_layer.sourceCrs())
    pr = new_layer.dataProvider()
    _write_data(new_layer, input_layer, mapping)
    new_layer.updateExtents()
    QgsVectorFileWriter.writeAsVectorFormat(
        new_layer, output_file, "utf-8", destCRS=input_layer.sourceCrs(),
        driverName="ESRI Shapefile")

    vl = QgsVectorLayer(output_file, layer_name, "ogr")
    QgsProject.instance().addMapLayer(vl)

def _write_data(target_layer, input_layer, mapping):

    pr = target_layer.dataProvider()
    for feature in input_layer.getFeatures():
        new_fet = QgsFeature()
        point = feature.geometry().asPoint()
        geom = QgsGeometry.fromPointXY(QgsPointXY(point.x(), point.y()))
        new_fet.setGeometry(geom)
        new_fet.setFields(target_layer.fields())
        for attr in mapping:
            new_fet.setAttribute(attr, feature.attribute(mapping[attr]))
        pr.addFeature(new_fet)


def _create_layer(data_type, layer_name, crs):

    uri = "{geom}?crs=epsg:{srid}&index=yes".format(
        srid=crs.postgisSrid(),
        geom=data_type["geometry"]["type"],
    )
    uri = QgsDataSourceUri(uri)

    vl = QgsVectorLayer(uri.uri(), layer_name, "memory")
    pr = vl.dataProvider()
    vl.setCrs(QgsCoordinateReferenceSystem(crs.postgisSrid()))

    attributes = []
    for attrib in data_type["properties"]:
        attributes.append(QgsField(attrib, data_type["properties"][attrib][0]))
    pr.addAttributes(attributes)
    vl.updateFields()
    return vl

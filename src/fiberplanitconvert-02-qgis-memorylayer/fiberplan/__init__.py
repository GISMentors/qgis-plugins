from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import QVariant
import os
from collections import OrderedDict


DATA_TYPES = {
    "demand_points": {
        "geometry": {
            "type": "Point"
        },
        "properties": OrderedDict([
            ("gistool_id", QVariant.Int),
            ("include", QVariant.Bool),
            ("connection", QVariant.String),
            ("pon_adop", QVariant.Double),
            ("p2p_adop", QVariant.Double),
            ("pon_homes", QVariant.Int),
            ("p2p_homes", QVariant.Int),
            ("pon_m_rev", QVariant.Double),
            ("p2p_m_rev", QVariant.Double),
            ("bldg_id", QVariant.String),
            ("streetname", QVariant.String),
            ("identifier", QVariant.String),
            ("floorcount", QVariant.Int),
            ("locked", QVariant.Bool),
            ("forced_cbl", QVariant.String)
        ])
    }
}

def convert(input_layer, mapping_file, target_data_type):
    """Convert input data file to target shapefile
    """

    mapping = _get_mapping_data(mapping_file)
    new_layer = _get_new_layer(target_data_type)
    pr = new_layer.dataProvider()
    _write_data(new_layer, input_layer, mapping)
    new_layer.updateExtents()
    QgsProject.instance().addMapLayer(new_layer)

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

def _get_new_layer(data_type):

    uri = "{geom}?index=yes".format(
        geom=DATA_TYPES[data_type]["geometry"]["type"],
    )

    vl = QgsVectorLayer(uri, data_type, "memory")
    pr = vl.dataProvider()

    attributes = []
    for attrib in DATA_TYPES[data_type]["properties"]:
        attributes.append(QgsField(attrib, DATA_TYPES[data_type]["properties"][attrib]))
    pr.addAttributes(attributes)
    vl.updateFields()
    return vl

def _get_mapping_data(file_name):

    data = {}
    with open(file_name) as mapping:
        for line in mapping.readlines():
            src, dest = line.strip().split(",")
            src = src.strip()
            dest = dest.strip()

            data[dest] = src

    return data

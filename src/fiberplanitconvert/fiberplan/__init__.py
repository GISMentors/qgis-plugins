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
            ("gistool_id", (QVariant.Int, "int")),
            ("include", (QVariant.Bool, "bool")),
            ("connection", (QVariant.String, "str")),
            ("pon_adop", (QVariant.Double, "float")),
            ("p2p_adop", (QVariant.Double, "float")),
            ("pon_homes", (QVariant.Int, "int")),
            ("p2p_homes", (QVariant.Int, "int")),
            ("pon_m_rev", (QVariant.Double, "float")),
            ("p2p_m_rev", (QVariant.Double, "float")),
            ("bldg_id", (QVariant.String, "str")),
            ("streetname", (QVariant.String, "str")),
            ("identifier", (QVariant.String, "str")),
            ("floorcount", (QVariant.Int, "int")),
            ("locked", (QVariant.Bool, "bool")),
            ("forced_cbl", (QVariant.String, "str"))
        ])
    }
}

def convert(tool, input_layer, mapping_file, target_data_type, output_file):
    """Convert input data file to target shapefile
    """

    mapping = _get_mapping_data(mapping_file)
    data_type = DATA_TYPES[target_data_type]

    if tool == "qgis":
        from .qgis_convertor import convert as target_convert
    else:
        from .fiona_convertor import convert as target_convert

    return target_convert(input_layer, mapping, data_type, target_data_type, output_file)




def _get_mapping_data(file_name):

    data = {}
    with open(file_name) as mapping:
        for line in mapping.readlines():
            src, dest = line.strip().split(",")
            src = src.strip()
            dest = dest.strip()

            data[dest] = src

    return data


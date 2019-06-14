from qgis.core import *
from urllib.parse import urlparse
import fiona
import csv


def convert(input_layer, mapping, data_type, layer_name, output_file):
    """Convert input data using fiona
    """
    input_file_name = urlparse(input_layer.dataProvider().dataSourceUri()).path
    data = []
    with open(input_file_name) as csvf:
        reader = csv.reader(csvf, delimiter=";")
        headers = next(reader)
        headers = {h: headers.index(h) for h in headers}
        for line in reader:
            (
                myid, adres_opgevoerd_datum, adres_opgevoerd_door,
                laatste_update_ISP, update_ISP, laatste_update_bouw,
                update_bouw, aansluitadres_postcode, aansluitadres_straatnaam,
                aansluitadres_huisnummer, aansluitadres_toevoeging,
                aansluitadres_kamer, aansluitadres_plaatsnaam,
                aansluitadres_buurtschap, aansluitadres_gemeente, area_id,
                aansluit_type, opmerking, netwerk_eigenaar, bag_ID,
                BAG_gebruiksdoel, X, Y, enable, disable_opmerking,
                disable_datum, disable_gebruiker, fiber_only, klant_nummer,
                isp_contract, RFS_status, Initiele_claimdatum, provider_name,
                opleverstatus, Start_HP_plastic, Indicatie_datum_HP_plastic,
                Opleverdatum_HP_plastic, Indicatie_datum_HC_gereed, HAS_datum,
                HC_gereed_datum, bouwer, area_status, LC, WP, kastCIF,
                ODFladeCIF, PPCIF, kastOO, ODFladeOO, PPOO, locatie_klantzijde,
                ambassadeur
            ) = line

            feature = {
                "type": "Feature",
                "properties": {k: None for k in data_type["properties"]},
                "geometry": {
                    "type": data_type["geometry"]["type"],
                    "coordinates": [float(X), float(Y)]
                }
            }
            for attr in mapping:
                feature["properties"][attr] = _get_attrib_with_type(
                    attr,
                    data_type,
                    line[headers[mapping[attr]]]
                )
            data.append(feature)

        schema = {
            'geometry': data_type["geometry"]["type"],
            'properties': {}
        }

    for attrib in data_type["properties"]:
        schema["properties"][attrib] = data_type["properties"][attrib][1]

    with fiona.open(output_file, "w", driver="ESRI Shapefile",
                    crs="EPSG:{}".format(
                        input_layer.sourceCrs().postgisSrid()
                    ), schema=schema) as c:
        c.writerecords(data)

    vl = QgsVectorLayer(output_file, layer_name, "ogr")
    QgsProject.instance().addMapLayer(vl)


def _get_attrib_with_type(attribute, data_type, data):

    convertors = {
        "int": int,
        "float": float,
        "str": str,
        "bool": bool
    }

    return convertors[
            data_type["properties"][attribute][1]
        ](data)

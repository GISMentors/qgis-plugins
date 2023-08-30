import sys
sys.path.insert(0, '/usr/lib/grass76/etc/python')

import grass.script as gs
import grass.script.setup as gsetup

gsetup.init('/tmp', 'qgis_test', 'PERMANENT')
gs.create_location('/tmp', 'qgis_test', epsg=4326)
print (gs.gisenv())
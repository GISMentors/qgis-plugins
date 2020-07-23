# příklad souboru ~/.local/share/QGIS/QGIS3/startup.py

#
# přídání vlastní cesty  k Python modulům
#
import sys
sys.path.append("/home/user/python/moduly")

#
# aktivace vlastního Virtualenv z Pythonu
#
activate_this_file = "/cesta/k/virtualenv/bin/activate_this.py"
exec(
    compile(
        open(activate_this_file, "rb").read(),
        activate_this_file, 'exec'
    ),
    dict(__file__=activate_this_file)
)


#
# případná instalace chybějících balíků
#
import pip
pip.main(['install', 'some_package'])

#
# ověření přítomnosti balíků
#
try:
    import fiona
    print("Vše v pořádku")
except ImportError as e:
    print("Fiona není nainstalována")

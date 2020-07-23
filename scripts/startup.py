# file example ~/.local/share/QGIS/QGIS3/startup.py

#
# adding custom path to Python plugins
#
import sys
sys.path.append("/home/user/python/plugins")

#
# activation of your Virtualenv
#
activate_this_file = "/path/to/virtualenv/bin/activate_this.py"
exec(
    compile(
        open(activate_this_file, "rb").read(),
        activate_this_file, 'exec'
    ),
    dict(__file__=activate_this_file)
)


#
# installation of missing packages
#
import pip
pip.main(['install', 'some_package'])

#
# checking presence of the packages
#
try:
    import fiona
    print("Everything is okay")
except ImportError as e:
    print("Fiona is not installed")

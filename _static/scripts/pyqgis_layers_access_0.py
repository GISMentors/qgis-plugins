for layer in QgsProject.instance().mapLayers().values():
    if layer.type() == QgsMapLayer.VectorLayer:
        print (layer.name(), layer.featureCount())
    else:
        print (layer.name())

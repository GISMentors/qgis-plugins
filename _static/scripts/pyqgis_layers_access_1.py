for layer in QgsProject.instance().mapLayers().values():
    if not QgsProject.instance().layerTreeRoot().findLayer(layer.id()).itemVisibilityChecked():
        continue

    if layer.type() != QgsMapLayer.VectorLayer or layer.wkbType() != QgsWkbTypes.MultiPolygon:
        continue
  
    print (layer.name(), layer.featureCount())
    for feat in layer.getFeatures():
        geom = feat.geometry()
        try:
            nazev = feat['nazev']
        except KeyError:
            nazev = 'no name defined'
            
        print ('{0}: {1} {2:.1f} ha'.format(feat.id(), nazev, geom.area()/1e4))

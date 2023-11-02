def save_views(output_path):
    """
    save graphical output for every row in attribute table
    """
    canvas = iface.mapCanvas()
    layer = canvas.currentLayer()
        
    for feature in layer.getFeatures():
        layer.selectByIds([feature.id()])
        canvas.setSelectionColor(QColor("transparent"))
        box = layer.boundingBoxOfSelected()
        iface.mapCanvas().setExtent(box)
        pixmap = QPixmap(canvas.mapSettings().outputSize().width(),
                         canvas.mapSettings().outputSize().height()
        )
        mapfile = os.path.join(
                output_path,
               '{0}_{1:03d}.png'.format(layer.name(), feature.id())
        )
        iface.mapCanvas().saveAsImage(mapfile, pixmap)
        layer.removeSelection()

    # save also full extend of vector layer                            
    canvas.setExtent(layer.extent())
    pixmap = QPixmap(canvas.mapSettings().outputSize().width(),
                     canvas.mapSettings().outputSize().height()
    )
    mapfile = os.path.join(
        output_path,
        '{}_full.png'.format(layer.name())
    )
    canvas.saveAsImage(mapfile, pixmap)
        
save_views("/tmp/")

from PySide import QtGui

import ui

ui_file_name = 'layer_widget.ui'
class LayerWidget(QtGui.QWidget):
    def __init__(self, *args):
        apply(QtGui.QWidget.__init__, (self,) + args)
        self.myWidget = ui.load_ui_from_file(ui_file_name)

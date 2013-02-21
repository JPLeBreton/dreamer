from PySide import QtGui
from PySide import QtCore
from PySide import QtUiTools

from pyside_dynamic import loadUi
import ui
from layer_widget import LayerWidget

ui_file_name = 'main_window.ui'
class MainWindow(QtGui.QMainWindow):
    def __init__(self, *args):
        QtGui.QMainWindow.__init__(self)
        loadUi(ui.UI_RESOURCE_PATH + ui_file_name, self)
        
        self._layer_widget = LayerWidget(self)
        self.layer_dock.setWidget(self._layer_widget)
    
    @QtCore.Slot()
    def _on_action_new_layer(self):
        self._layer_widget.new_layer()

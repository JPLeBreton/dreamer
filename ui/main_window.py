from PySide import QtGui
from PySide import QtCore
from PySide import QtUiTools

from ui import UI_RESOURCE_PATH

ui_file_name = 'main_window.ui'
class MainWindow(QtGui.QMainWindow):
    def __init__(self, *args):
        apply(QtGui.QMainWindow.__init__, (self,) + args)
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile(UI_RESOURCE_PATH + ui_file_name)
        ui_file.open(QtCore.QFile.ReadOnly)
        self.myWindow = loader.load(ui_file)
        ui_file.close()
        self.setCentralWidget(self.myWindow)

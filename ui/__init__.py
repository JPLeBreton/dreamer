from PySide import QtCore
from PySide import QtUiTools

UI_RESOURCE_PATH = 'ui/resources/'

def load_ui_from_file(filename):
    loader = QtUiTools.QUiLoader()
    ui_file = QtCore.QFile(UI_RESOURCE_PATH + filename)
    ui_file.open(QtCore.QFile.ReadOnly)
    widget = loader.load(ui_file)
    ui_file.close()
    return widget

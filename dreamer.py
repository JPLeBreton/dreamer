import sys
from PySide.QtGui import QApplication

from ui.main_window import MainWindow

APP_NAME = 'Dreamer'

class DreamerApp(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        self.setApplicationName(APP_NAME)

app = DreamerApp(sys.argv)

if __name__ == "__main__":
    window = MainWindow()
    window.setWindowTitle(APP_NAME)
    window.show()
    return_code = app.exec_()
    sys.exit(return_code)

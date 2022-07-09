import sys

from qt_pycode.ui_scoopgui import *

# from PySide6 import *

from qt_material import *

from PySide6 import QtWidgets

from PySide6.QtCore import *

from PySide6.QtGui import *

from PySide6.QtSvgWidgets import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.search_page_button = QPushButton(
            "background-color: rgb(255, 0, 0);"
        )
        self.ui.load_pages.enter_search_layout.addWidget(self.search_page_button, Qt.AlignCenter, Qt.AlignCenter)


app = QtWidgets.QApplication(sys.argv)
# apply_stylesheet(app, theme='dark_teal.xml')
# app.setStyle('dark_amber.xml')
window = MainWindow()
window.show()
app.exec()
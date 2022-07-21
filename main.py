import sys

from qt_pycode.ui_scoopgui import *

from qt_material import *

from PySide6 import QtWidgets

from PySide6.QtCore import *

from PySide6.QtGui import *

from PySide6.QtSvgWidgets import *

from PySide6.QtWidgets import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.search_page_button = QPushButton('Search', parent=self)
        self.manage_apps_button = QtWidgets.QPushButton('Apps', parent=self)
        self.manage_buckets_button = QtWidgets.QPushButton('Buckets', parent=self)
        self.enter_search_layout.addWidget(self.search_page_button, Qt.AlignCenter, Qt.AlignCenter)
        self.enter_manage_apps_layout.addWidget(self.manage_apps_button, Qt.AlignCenter, Qt.AlignCenter)
        self.enter_manage_buckets_layout.addWidget(self.manage_buckets_button, Qt.AlignCenter, Qt.AlignCenter)
        self.search_page_button.clicked.connect(lambda: print('Search'))
        self.manage_apps_button.clicked.connect(lambda: print('Manage Apps'))
        self.manage_buckets_button.clicked.connect(lambda: print('Manage Buckets'))
        with open('widgets/push_button.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Scoop GUI')
my_pixmap = QPixmap("scoopicon.ico")
my_icon = QIcon(my_pixmap)
window.setWindowIcon(my_icon)
window.show()
app.exec()

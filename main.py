import sys

from qt_pycode.ui_scoopgui import *

from qt_material import *

from PySide6 import QtWidgets

from PySide6.QtCore import *

from PySide6.QtGui import *

from PySide6.QtSvgWidgets import *

from PySide6.QtWidgets import *

import subprocess

import re

POWERSHELL_PATH = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.search_page_button = QPushButton('Search', parent=self)
        self.manage_apps_button = QtWidgets.QPushButton('Installed', parent=self)
        self.manage_buckets_button = QtWidgets.QPushButton('Buckets', parent=self)
        self.enter_search_layout.addWidget(self.search_page_button, Qt.AlignCenter, Qt.AlignCenter)
        self.enter_manage_apps_layout.addWidget(self.manage_apps_button, Qt.AlignCenter, Qt.AlignCenter)
        self.enter_manage_buckets_layout.addWidget(self.manage_buckets_button, Qt.AlignCenter, Qt.AlignCenter)
        self.search_page_button.clicked.connect(self.goSearch)
        self.manage_apps_button.clicked.connect(self.goInstalled)
        self.manage_buckets_button.clicked.connect(self.goBuckets)
        with open('widgets/push_button.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def goSearch(self):
        print("Search")
        self.stackedWidget.setCurrentWidget(self.search)

    def goInstalled(self):
        print("Manage Apps")
        self.stackedWidget.setCurrentWidget(self.installed)

    def goBuckets(self):
        print("Manage Buckets")
        self.stackedWidget.setCurrentWidget(self.buckets)
        blayout = QFormLayout()
        blayout.addWidget(QLabel(""))
        commandline_options = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop bucket list']
        process_result = subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        universal_newlines=True)
        res = process_result.stdout.split()

        # Remove numbers from list
        res = [x for x in res if not (x.isdigit()
                                                 or x[0] == '-' and x[1:].isdigit())]

        # Remove - from list
        for idx, ele in enumerate(res):
           res[idx] = ele.replace('-', '')

        #Remove blank spaces in list
        while ("" in res):
            res.remove("")

        # Remove dates from list
        res = list(filter(
            lambda ThisWord: not re.match('^(?:(?:[0-9]{2}[:\/,]){2}[0-9]{2,4}|am|pm)$', ThisWord),
            res))

        # Remove needless detail from list
        stopwords = ['Name', 'Source', 'Updates', 'Manifests', 'main', 'Updated']
        for word in list(res):
            if word in stopwords:
                res.remove(word)


        # Only bucket names stay
        i = int(0)
        while True:
            try:
                i = i + 1
                del res[i]
            except:
                break

        print(res)
        endres = ""
        for ele in res:
            endres += ele + " "
        blayout.addWidget(QLabel(endres))
        self.buckets.setLayout(blayout)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Scoop GUI')
my_pixmap = QPixmap("scoopicon.ico")
my_icon = QIcon(my_pixmap)
window.setWindowIcon(my_icon)
window.show()
app.exec()

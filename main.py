import sys

from qt_pycode.ui_scoopgui import *

from PySide6.QtGui import *

import subprocess

import re

from PySide6 import QtCore, QtWidgets, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

POWERSHELL_PATH = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget, QMessageBox, QComboBox)

from state_tooltip import StateTooltip

from threading import Thread

import time

from py_toggle import *

###################################################################################################################
#####   https://tenor.com/view/calculating-puzzled-math-confused-confused-look-gif-14677181                    ####

#####   U S E -  C O M M E N TS - literally me when i was trying to understand spaghetti without comments     #####

#####   https://tenor.com/view/calculating-puzzled-math-confused-confused-look-gif-14677181                    ###
###################################################################################################################

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None , *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs, parent=parent)
        self.setupUi(self)
        self.search_page_button = QPushButton('Search', parent=self)
        self.manage_apps_button = QtWidgets.QPushButton('Installed', parent=self)
        self.manage_buckets_button = QtWidgets.QPushButton('Buckets', parent=self)

        # settings page
        self.settings_page_button = QtWidgets.QPushButton('le Settings', parent=self)
        self.settings_page_layout.addWidget(self.settings_page_button, Qt.AlignCenter, Qt.AlignCenter)
        self.settings_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page) )


        self.enter_search_layout.addWidget(self.search_page_button, Qt.AlignCenter, Qt.AlignCenter)
        self.enter_manage_apps_layout.addWidget(self.manage_apps_button, Qt.AlignCenter, Qt.AlignCenter)
        self.enter_manage_buckets_layout.addWidget(self.manage_buckets_button, Qt.AlignCenter, Qt.AlignCenter)
        self.search_page_button.clicked.connect(self.goSearch)
        self.manage_apps_button.clicked.connect(self.goInstalled)
        self.manage_buckets_button.clicked.connect(self.goBuckets)

        # settings page

        # download manager setting - aria2c
        self.thing = PyToggle(
            width=50
        )
        # fast search - scoop-search
        self.another_thing = PyToggle(
            width=50
        )
        # something else
        self.a_thing = PyToggle(
            width=50
        )

        self.settings_toggle_1_layout.addWidget(self.thing, Qt.AlignCenter, Qt.AlignCenter)
        self.settings_toggle_2_layout.addWidget(self.another_thing, Qt.AlignCenter, Qt.AlignCenter)
        self.settings_toggle_3_layout.addWidget(self.a_thing, Qt.AlignCenter, Qt.AlignCenter)


        # self.stateTooltip = None
        with open('resource/pushbutton/push_button.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def goSearch(self):
        print("Search")
        self.stackedWidget.setCurrentWidget(self.search)

    def goInstalled(self):
        print("Manage Apps")
        self.stackedWidget.setCurrentWidget(self.installed)

    def goBuckets(self):
        self.stackedWidget.setCurrentWidget(self.buckets)


        def function():
            commandline_options = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop bucket list']
            process_result = subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
            res = process_result.stdout.split()

            # Manipulate list
            ################################################################################################################

            res = [x for x in res if not (x.isdigit()
                                                     or x[0] == '-' and x[1:].isdigit())]

            for idx, ele in enumerate(res):
               res[idx] = ele.replace('-', '')

            while ("" in res):
                res.remove("")

            res = list(filter(
                lambda ThisWord: not re.match('^(?:(?:[0-9]{2}[:\/,]){2}[0-9]{2,4}|am|pm)$', ThisWord),
                res))

            stopwords = ['Name', 'Source', 'Manifests', 'main', 'Updated']
            for word in list(res):
                if word in stopwords:
                    res.remove(word)

            res = [elements for elements in res if '/Main' not in elements]

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
                endres += ele + "\n"

            ################################################################################################################


            self.list_buckets_label = QLabel(endres, parent=self)
            self.list_buckets_label.setFont(QFont('Arial', 12))
            self.list_buckets_layout.addWidget(self.list_buckets_label, Qt.AlignLeft, Qt.AlignTop)
            self.bucket_button_add.clicked.connect(self.addBucket)
            self.bucket_button_remove.clicked.connect(self.removeBucket)

            # back button
            self.bucket_goback.clicked.connect(self.gohomeb)
            self.bucket_goback_2.clicked.connect(self.gohomeb)

            self.cb.addItems(res)
            # self.stateTooltip = None
            with open('resource/statetooltip/style/demo.qss', encoding='utf-8') as f:
                self.setStyleSheet(f.read())

        # thread fixes hanging, daemon keep alive until finished
        t = Thread(target=function)
        t.daemon = True
        t.start()

    def addBucket(self):
        # if self.stateTooltip:
        #     self.stateTooltip.setContent('Complete')
        #     self.stateTooltip.setState(True)
        #     self.stateTooltip = None
        # else:
        #     self.stateTooltip = StateTooltip('Process', 'Loading', self)
        #     self.stateTooltip.move(510, 30)
        #     self.stateTooltip.show()
        bucketname = self.bucket_input_add.text()
        # self.stackedWidget.setCurrentWidget(self.buckets)
        command = 'scoop bucket add ' + str(bucketname)
        commandline_options = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', command]
        process_result = subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        universal_newlines=True)
        choice = QtWidgets.QMessageBox.question(self, 'Finished',
                                                "We're not sure if the process was successful \nReload Buckets?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.list_buckets_layout.removeWidget(self.list_buckets_label)
            self.stackedWidget.setCurrentWidget(self.home)
            self.stackedWidget.setCurrentWidget(self.buckets)
        else:
            self.list_buckets_layout.removeWidget(self.list_buckets_label)
            self.stackedWidget.setCurrentWidget(self.home)

    def removeBucket(self):
        bucketname = self.cb.currentText()
        command = 'scoop bucket rm ' + str(bucketname)
        commandline_options = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', command]
        process_result = subprocess.run(commandline_options, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        universal_newlines=True)
        choice = QtWidgets.QMessageBox.question(self, 'Finished',
                                                "We're not sure if the process was successful \nReload Buckets?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.list_buckets_layout.removeWidget(self.list_buckets_label)
            self.stackedWidget.setCurrentWidget(self.home)
            self.stackedWidget.setCurrentWidget(self.buckets)
        else:
            self.list_buckets_layout.removeWidget(self.list_buckets_label)
            self.stackedWidget.setCurrentWidget(self.home)


    def gohomeb(self):
        self.list_buckets_layout.removeWidget(self.list_buckets_label)
        self.stackedWidget.setCurrentWidget(self.home)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Scoop GUI')
my_pixmap = QPixmap("scoopicon.ico")
my_icon = QIcon(my_pixmap)
window.setWindowIcon(my_icon)
window.show()
app.exec()
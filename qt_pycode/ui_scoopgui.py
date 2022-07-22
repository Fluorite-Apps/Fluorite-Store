# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoopguiGVrVtu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, -21, 1071, 601))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 230, 220, 145))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.enter_search_layout = QHBoxLayout(self.frame)
        self.enter_search_layout.setSpacing(0)
        self.enter_search_layout.setObjectName(u"enter_search_layout")
        self.enter_search_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(420, 230, 220, 145))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.enter_manage_apps_layout = QHBoxLayout(self.frame_2)
        self.enter_manage_apps_layout.setSpacing(0)
        self.enter_manage_apps_layout.setObjectName(u"enter_manage_apps_layout")
        self.enter_manage_apps_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(670, 230, 220, 145))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.enter_manage_buckets_layout = QHBoxLayout(self.frame_3)
        self.enter_manage_buckets_layout.setSpacing(0)
        self.enter_manage_buckets_layout.setObjectName(u"enter_manage_buckets_layout")
        self.enter_manage_buckets_layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.home)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(-20, 80, 1101, 41))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(18)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.home)
        self.buckets = QWidget()
        self.buckets.setObjectName(u"buckets")
        self.stackedWidget.addWidget(self.buckets)
        self.installed = QWidget()
        self.installed.setObjectName(u"installed")
        self.stackedWidget.addWidget(self.installed)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.stackedWidget.addWidget(self.search)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(-20, 550, 1091, 31))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.enter_search_layout_2 = QHBoxLayout(self.frame_4)
        self.enter_search_layout_2.setSpacing(0)
        self.enter_search_layout_2.setObjectName(u"enter_search_layout_2")
        self.enter_search_layout_2.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Scoop GUI", None))
    # retranslateUi


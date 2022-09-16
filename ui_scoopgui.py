# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoopguiTvrcEd.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)
import resource_file_qt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1146, 685)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, -1, 1171, 701))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.search_layout = QFrame(self.home)
        self.search_layout.setObjectName(u"search_layout")
        self.search_layout.setGeometry(QRect(509, 200, 251, 91))
        self.search_layout.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_layout.setStyleSheet(u"QPushButton {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.search_layout.setFrameShape(QFrame.NoFrame)
        self.search_layout.setFrameShadow(QFrame.Raised)
        self.search_layout.setLineWidth(0)
        self.enter_search_layout = QHBoxLayout(self.search_layout)
        self.enter_search_layout.setSpacing(0)
        self.enter_search_layout.setObjectName(u"enter_search_layout")
        self.enter_search_layout.setContentsMargins(0, 0, 0, 0)
        self.recommend_apps_frame = QFrame(self.home)
        self.recommend_apps_frame.setObjectName(u"recommend_apps_frame")
        self.recommend_apps_frame.setGeometry(QRect(509, 300, 251, 91))
        self.recommend_apps_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.recommend_apps_frame.setStyleSheet(u"QPushButton {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.recommend_apps_frame.setFrameShape(QFrame.NoFrame)
        self.recommend_apps_frame.setFrameShadow(QFrame.Raised)
        self.recommend_apps_frame.setLineWidth(0)
        self.enter_recommended_apps_frame = QHBoxLayout(self.recommend_apps_frame)
        self.enter_recommended_apps_frame.setSpacing(0)
        self.enter_recommended_apps_frame.setObjectName(u"enter_recommended_apps_frame")
        self.enter_recommended_apps_frame.setContentsMargins(0, 0, 0, 0)
        self.settings_frame = QFrame(self.home)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setGeometry(QRect(509, 400, 251, 91))
        self.settings_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_frame.setStyleSheet(u"QPushButton {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.settings_frame.setFrameShape(QFrame.NoFrame)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.settings_frame.setLineWidth(0)
        self.settings_page_layout = QHBoxLayout(self.settings_frame)
        self.settings_page_layout.setSpacing(0)
        self.settings_page_layout.setObjectName(u"settings_page_layout")
        self.settings_page_layout.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.home)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(330, 90, 441, 91))
        self.label_19.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_20 = QLabel(self.home)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(330, 300, 171, 91))
        self.label_20.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_4 = QLabel(self.home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 230, 141, 31))
        self.label_4.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_4.setWordWrap(True)
        self.title_3 = QLabel(self.home)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(370, 120, 351, 41))
        font = QFont()
        font.setPointSize(16)
        self.title_3.setFont(font)
        self.title_3.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.title_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 430, 131, 31))
        self.label_5.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_21 = QLabel(self.home)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(330, 400, 171, 91))
        self.label_21.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_23 = QLabel(self.home)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(330, 200, 171, 91))
        self.label_23.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_24 = QLabel(self.home)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(290, 70, 521, 551))
        self.label_24.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_6 = QLabel(self.home)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 330, 141, 31))
        self.label_6.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_6.setWordWrap(True)
        self.label_10 = QLabel(self.home)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(350, 530, 131, 31))
        self.label_10.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_10.setWordWrap(True)
        self.manage_appsbuckets_frame_2 = QFrame(self.home)
        self.manage_appsbuckets_frame_2.setObjectName(u"manage_appsbuckets_frame_2")
        self.manage_appsbuckets_frame_2.setGeometry(QRect(509, 500, 251, 91))
        self.manage_appsbuckets_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.manage_appsbuckets_frame_2.setStyleSheet(u"QPushButton {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.manage_appsbuckets_frame_2.setFrameShape(QFrame.NoFrame)
        self.manage_appsbuckets_frame_2.setFrameShadow(QFrame.Raised)
        self.manage_appsbuckets_frame_2.setLineWidth(0)
        self.enter_manage_buckets_layout = QHBoxLayout(self.manage_appsbuckets_frame_2)
        self.enter_manage_buckets_layout.setSpacing(0)
        self.enter_manage_buckets_layout.setObjectName(u"enter_manage_buckets_layout")
        self.enter_manage_buckets_layout.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.home)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(330, 500, 171, 91))
        self.label_57.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.stackedWidget.addWidget(self.home)
        self.label_24.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_23.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.title_3.raise_()
        self.search_layout.raise_()
        self.settings_frame.raise_()
        self.manage_appsbuckets_frame_2.raise_()
        self.label_57.raise_()
        self.label_10.raise_()
        self.recommend_apps_frame.raise_()
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.manage_buckets_frame_2 = QFrame(self.settings_page)
        self.manage_buckets_frame_2.setObjectName(u"manage_buckets_frame_2")
        self.manage_buckets_frame_2.setGeometry(QRect(570, 240, 131, 71))
        self.manage_buckets_frame_2.setStyleSheet(u"")
        self.manage_buckets_frame_2.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_2.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_2.setLineWidth(0)
        self.settings_toggle_1_layout = QHBoxLayout(self.manage_buckets_frame_2)
        self.settings_toggle_1_layout.setSpacing(0)
        self.settings_toggle_1_layout.setObjectName(u"settings_toggle_1_layout")
        self.settings_toggle_1_layout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.settings_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(330, 230, 171, 91))
        self.label_11.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_12 = QLabel(self.settings_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(330, 330, 171, 91))
        self.label_12.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_13 = QLabel(self.settings_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(330, 430, 171, 91))
        self.label_13.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.manage_buckets_frame_3 = QFrame(self.settings_page)
        self.manage_buckets_frame_3.setObjectName(u"manage_buckets_frame_3")
        self.manage_buckets_frame_3.setGeometry(QRect(570, 340, 131, 71))
        self.manage_buckets_frame_3.setStyleSheet(u"")
        self.manage_buckets_frame_3.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_3.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_3.setLineWidth(0)
        self.settings_toggle_2_layout = QHBoxLayout(self.manage_buckets_frame_3)
        self.settings_toggle_2_layout.setSpacing(0)
        self.settings_toggle_2_layout.setObjectName(u"settings_toggle_2_layout")
        self.settings_toggle_2_layout.setContentsMargins(0, 0, 0, 0)
        self.manage_buckets_frame_4 = QFrame(self.settings_page)
        self.manage_buckets_frame_4.setObjectName(u"manage_buckets_frame_4")
        self.manage_buckets_frame_4.setGeometry(QRect(570, 440, 131, 71))
        self.manage_buckets_frame_4.setStyleSheet(u"")
        self.manage_buckets_frame_4.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_4.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_4.setLineWidth(0)
        self.settings_toggle_3_layout = QHBoxLayout(self.manage_buckets_frame_4)
        self.settings_toggle_3_layout.setSpacing(0)
        self.settings_toggle_3_layout.setObjectName(u"settings_toggle_3_layout")
        self.settings_toggle_3_layout.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.settings_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(330, 120, 441, 91))
        self.label_14.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.title_2 = QLabel(self.settings_page)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(370, 150, 351, 41))
        self.title_2.setFont(font)
        self.title_2.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.title_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.settings_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 260, 81, 31))
        self.label.setStyleSheet(u"")
        self.label_2 = QLabel(self.settings_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 360, 141, 31))
        self.label_2.setStyleSheet(u"")
        self.label_3 = QLabel(self.settings_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 460, 131, 31))
        self.label_3.setStyleSheet(u"")
        self.label_15 = QLabel(self.settings_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(510, 230, 251, 91))
        self.label_15.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_16 = QLabel(self.settings_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(510, 330, 251, 91))
        self.label_16.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_17 = QLabel(self.settings_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(510, 430, 251, 91))
        self.label_17.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_18 = QLabel(self.settings_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(290, 100, 521, 471))
        self.label_18.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.back_button_frame_8 = QFrame(self.settings_page)
        self.back_button_frame_8.setObjectName(u"back_button_frame_8")
        self.back_button_frame_8.setGeometry(QRect(860, 580, 261, 61))
        self.back_button_frame_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_8.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(227, 219, 192);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_8.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_8.setFrameShadow(QFrame.Raised)
        self.back_button_frame_8.setLineWidth(0)
        self.return_home_layout = QHBoxLayout(self.back_button_frame_8)
        self.return_home_layout.setSpacing(0)
        self.return_home_layout.setObjectName(u"return_home_layout")
        self.return_home_layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.settings_page)
        self.label_18.raise_()
        self.label_17.raise_()
        self.label_16.raise_()
        self.label_15.raise_()
        self.manage_buckets_frame_2.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.manage_buckets_frame_3.raise_()
        self.manage_buckets_frame_4.raise_()
        self.label_14.raise_()
        self.title_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.back_button_frame_8.raise_()
        self.splashscreen = QWidget()
        self.splashscreen.setObjectName(u"splashscreen")
        self.label_60 = QLabel(self.splashscreen)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(250, 70, 531, 551))
        self.label_60.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_63 = QLabel(self.splashscreen)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(280, 220, 461, 301))
        self.label_63.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_4 = QLabel(self.splashscreen)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(320, 140, 351, 41))
        self.title_4.setFont(font)
        self.title_4.setStyleSheet(u"")
        self.title_4.setAlignment(Qt.AlignCenter)
        self.label_66 = QLabel(self.splashscreen)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(290, 110, 441, 91))
        self.label_66.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_69 = QLabel(self.splashscreen)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(280, 540, 471, 71))
        self.label_69.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_6 = QLabel(self.splashscreen)
        self.title_6.setObjectName(u"title_6")
        self.title_6.setGeometry(QRect(280, 550, 461, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.title_6.setFont(font1)
        self.title_6.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.title_6.setAlignment(Qt.AlignCenter)
        self.label_72 = QLabel(self.splashscreen)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(360, 260, 291, 241))
        self.label_72.setStyleSheet(u"")
        self.label_72.setPixmap(QPixmap(u":/images/scoop.png"))
        self.label_72.setScaledContents(True)
        self.stackedWidget.addWidget(self.splashscreen)
        self.label_60.raise_()
        self.label_63.raise_()
        self.label_66.raise_()
        self.title_4.raise_()
        self.label_69.raise_()
        self.title_6.raise_()
        self.label_72.raise_()
        self.buckets = QWidget()
        self.buckets.setObjectName(u"buckets")
        self.title_buckets = QLabel(self.buckets)
        self.title_buckets.setObjectName(u"title_buckets")
        self.title_buckets.setGeometry(QRect(140, 60, 291, 41))
        self.title_buckets.setFont(font)
        self.title_buckets.setStyleSheet(u"")
        self.title_buckets.setAlignment(Qt.AlignCenter)
        self.add_bucket_title = QLabel(self.buckets)
        self.add_bucket_title.setObjectName(u"add_bucket_title")
        self.add_bucket_title.setGeometry(QRect(60, 130, 221, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.add_bucket_title.setFont(font2)
        self.add_bucket_title.setStyleSheet(u"")
        self.add_bucket_title.setAlignment(Qt.AlignCenter)
        self.bucket_input_add = QLineEdit(self.buckets)
        self.bucket_input_add.setObjectName(u"bucket_input_add")
        self.bucket_input_add.setGeometry(QRect(50, 170, 261, 41))
        self.bucket_input_add.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* \u5355\u884c\u8f93\u5165\u6846 */\n"
"QLineEdit {\n"
"    padding: 8px 13px 7px 13px;\n"
"    font: 17px 'Microsoft YaHei';\n"
"    selection-background-color: rgb(0, 153, 188);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(0, 153, 188);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color: rgb(122, 122, 122);\n"
"    border: none;\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
"\n"
"/* \u53f3\u51fb\u83dc\u5355 */\n"
"QMenu {\n"
"    width: 1px;\n"
"    height: 1px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    font-size: 18px;\n"
"    font: 18px \"Microsoft YaHei\";\n"
"    padding: 5px 0px 5px 0px;\n"
"    border: 1px solid rgb(196, 199, 200);\n"
"}\n"
"\n"
"\n"
"QMenu::right-arrow {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    right: 16px;\n"
"    border-border-image: url(resource/images/\u5b50\u83dc\u5355\u53f3\u7bad\u5934.png);\n"
"\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    width: 140p"
                        "x;\n"
"    background: rgba(0, 0, 0, 104);\n"
"    margin-right: 13px;\n"
"    margin-top: 5px;\n"
"    margin-bottom: 5px;\n"
"    margin-left: 13;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 7px 20px 7px 26px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    border-width: 1px;\n"
"    border-color: rgb(212, 212, 212);\n"
"    background: rgba(0, 0, 0, 25);\n"
"    color: black;\n"
"}\n"
"\n"
"QMenu[hasCancelAct='true'] {\n"
"    width: 1px;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"    position: absolute;\n"
"    left: 16px;\n"
"}")
        self.bucket_button_add = QPushButton(self.buckets)
        self.bucket_button_add.setObjectName(u"bucket_button_add")
        self.bucket_button_add.setGeometry(QRect(320, 170, 201, 41))
        self.bucket_button_add.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.remove_bucket_title = QLabel(self.buckets)
        self.remove_bucket_title.setObjectName(u"remove_bucket_title")
        self.remove_bucket_title.setGeometry(QRect(0, 230, 321, 41))
        self.remove_bucket_title.setFont(font2)
        self.remove_bucket_title.setStyleSheet(u"")
        self.remove_bucket_title.setAlignment(Qt.AlignCenter)
        self.bucket_button_remove = QPushButton(self.buckets)
        self.bucket_button_remove.setObjectName(u"bucket_button_remove")
        self.bucket_button_remove.setGeometry(QRect(320, 280, 201, 41))
        self.bucket_button_remove.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"    padding: 10px 64px 10px 64px;\n"
"    font: 19px 'Microsoft YaHei';\n"
"    border: transparent;\n"
"    border-radius: 4px;\n"
"    /* height: 40px; */\n"
"}\n"
"\n"
"QPushButton:pressed:hover {\n"
"    background-color: rgb(153, 153, 153);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: rgb(204, 204, 204);\n"
"    color: rgb(122, 122, 122);\n"
"}")
        self.cb = QComboBox(self.buckets)
        self.cb.setObjectName(u"cb")
        self.cb.setGeometry(QRect(50, 280, 261, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.cb.setFont(font3)
        self.title_buckets_2 = QLabel(self.buckets)
        self.title_buckets_2.setObjectName(u"title_buckets_2")
        self.title_buckets_2.setGeometry(QRect(690, 50, 291, 41))
        font4 = QFont()
        font4.setFamilies([u"Arial Black"])
        font4.setPointSize(22)
        font4.setBold(True)
        self.title_buckets_2.setFont(font4)
        self.title_buckets_2.setAlignment(Qt.AlignCenter)
        self.label_46 = QLabel(self.buckets)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(30, 30, 521, 471))
        self.label_46.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_47 = QLabel(self.buckets)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(570, 30, 521, 471))
        self.label_47.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"			\n"
"			\n"
"	background-color: rgb(240, 249, 243);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_48 = QLabel(self.buckets)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(70, 40, 441, 81))
        self.label_48.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.title_buckets_3 = QLabel(self.buckets)
        self.title_buckets_3.setObjectName(u"title_buckets_3")
        self.title_buckets_3.setGeometry(QRect(680, 60, 291, 41))
        self.title_buckets_3.setFont(font)
        self.title_buckets_3.setStyleSheet(u"")
        self.title_buckets_3.setAlignment(Qt.AlignCenter)
        self.label_49 = QLabel(self.buckets)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(610, 40, 441, 81))
        self.label_49.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"			\n"
"			\n"
"	background-color: rgb(221, 232, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_50 = QLabel(self.buckets)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(610, 150, 151, 81))
        self.label_50.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"			\n"
"			\n"
"	background-color: rgb(221, 232, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_51 = QLabel(self.buckets)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(780, 150, 271, 81))
        self.label_51.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_52 = QLabel(self.buckets)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(780, 250, 271, 81))
        self.label_52.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_53 = QLabel(self.buckets)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(610, 250, 151, 81))
        self.label_53.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"			\n"
"			\n"
"	background-color: rgb(221, 232, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_54 = QLabel(self.buckets)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(780, 350, 271, 81))
        self.label_54.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_55 = QLabel(self.buckets)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(610, 350, 151, 81))
        self.label_55.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"			\n"
"			\n"
"	background-color: rgb(221, 232, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.title_buckets_4 = QLabel(self.buckets)
        self.title_buckets_4.setObjectName(u"title_buckets_4")
        self.title_buckets_4.setGeometry(QRect(610, 170, 151, 41))
        font5 = QFont()
        font5.setPointSize(12)
        self.title_buckets_4.setFont(font5)
        self.title_buckets_4.setStyleSheet(u"")
        self.title_buckets_4.setAlignment(Qt.AlignCenter)
        self.title_buckets_5 = QLabel(self.buckets)
        self.title_buckets_5.setObjectName(u"title_buckets_5")
        self.title_buckets_5.setGeometry(QRect(620, 370, 131, 41))
        self.title_buckets_5.setFont(font5)
        self.title_buckets_5.setStyleSheet(u"")
        self.title_buckets_5.setAlignment(Qt.AlignCenter)
        self.title_buckets_6 = QLabel(self.buckets)
        self.title_buckets_6.setObjectName(u"title_buckets_6")
        self.title_buckets_6.setGeometry(QRect(620, 270, 131, 41))
        self.title_buckets_6.setFont(font5)
        self.title_buckets_6.setStyleSheet(u"")
        self.title_buckets_6.setAlignment(Qt.AlignCenter)
        self.title_buckets_6.setWordWrap(True)
        self.update_all_apps_frame = QFrame(self.buckets)
        self.update_all_apps_frame.setObjectName(u"update_all_apps_frame")
        self.update_all_apps_frame.setGeometry(QRect(790, 160, 251, 61))
        self.update_all_apps_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_all_apps_frame.setStyleSheet(u"")
        self.update_all_apps_frame.setFrameShape(QFrame.NoFrame)
        self.update_all_apps_frame.setFrameShadow(QFrame.Raised)
        self.update_all_apps_frame.setLineWidth(0)
        self.update_all_apps_layout = QHBoxLayout(self.update_all_apps_frame)
        self.update_all_apps_layout.setSpacing(0)
        self.update_all_apps_layout.setObjectName(u"update_all_apps_layout")
        self.update_all_apps_layout.setContentsMargins(0, 0, 0, 0)
        self.remove_app_frame = QFrame(self.buckets)
        self.remove_app_frame.setObjectName(u"remove_app_frame")
        self.remove_app_frame.setGeometry(QRect(790, 360, 251, 61))
        self.remove_app_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.remove_app_frame.setStyleSheet(u"")
        self.remove_app_frame.setFrameShape(QFrame.NoFrame)
        self.remove_app_frame.setFrameShadow(QFrame.Raised)
        self.remove_app_frame.setLineWidth(0)
        self.remove_app_layout = QHBoxLayout(self.remove_app_frame)
        self.remove_app_layout.setSpacing(0)
        self.remove_app_layout.setObjectName(u"remove_app_layout")
        self.remove_app_layout.setContentsMargins(0, 0, 0, 0)
        self.not_added_yet = QFrame(self.buckets)
        self.not_added_yet.setObjectName(u"not_added_yet")
        self.not_added_yet.setGeometry(QRect(790, 260, 251, 61))
        self.not_added_yet.setCursor(QCursor(Qt.PointingHandCursor))
        self.not_added_yet.setStyleSheet(u"")
        self.not_added_yet.setFrameShape(QFrame.NoFrame)
        self.not_added_yet.setFrameShadow(QFrame.Raised)
        self.not_added_yet.setLineWidth(0)
        self.cleanup_old_app_versions_layout = QHBoxLayout(self.not_added_yet)
        self.cleanup_old_app_versions_layout.setSpacing(0)
        self.cleanup_old_app_versions_layout.setObjectName(u"cleanup_old_app_versions_layout")
        self.cleanup_old_app_versions_layout.setContentsMargins(0, 0, 0, 0)
        self.back_button_frame = QFrame(self.buckets)
        self.back_button_frame.setObjectName(u"back_button_frame")
        self.back_button_frame.setGeometry(QRect(820, 550, 261, 61))
        self.back_button_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(204, 222, 211);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame.setFrameShape(QFrame.NoFrame)
        self.back_button_frame.setFrameShadow(QFrame.Raised)
        self.back_button_frame.setLineWidth(0)
        self.bucket_back_layout = QHBoxLayout(self.back_button_frame)
        self.bucket_back_layout.setSpacing(0)
        self.bucket_back_layout.setObjectName(u"bucket_back_layout")
        self.bucket_back_layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.buckets)
        self.label_46.raise_()
        self.add_bucket_title.raise_()
        self.bucket_input_add.raise_()
        self.bucket_button_add.raise_()
        self.remove_bucket_title.raise_()
        self.bucket_button_remove.raise_()
        self.cb.raise_()
        self.title_buckets_2.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.title_buckets.raise_()
        self.label_49.raise_()
        self.title_buckets_3.raise_()
        self.label_50.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.label_54.raise_()
        self.label_55.raise_()
        self.title_buckets_4.raise_()
        self.title_buckets_5.raise_()
        self.title_buckets_6.raise_()
        self.update_all_apps_frame.raise_()
        self.remove_app_frame.raise_()
        self.not_added_yet.raise_()
        self.back_button_frame.raise_()
        self.installed = QWidget()
        self.installed.setObjectName(u"installed")
        self.stackedWidget.addWidget(self.installed)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.label_27 = QLabel(self.search)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(330, 70, 441, 51))
        self.label_27.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_28 = QLabel(self.search)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(60, 50, 1011, 601))
        self.label_28.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.search_box_frame = QFrame(self.search)
        self.search_box_frame.setObjectName(u"search_box_frame")
        self.search_box_frame.setGeometry(QRect(360, 70, 331, 51))
        self.search_box_frame.setStyleSheet(u"")
        self.search_box_frame.setFrameShape(QFrame.NoFrame)
        self.search_box_frame.setFrameShadow(QFrame.Raised)
        self.search_box_frame.setLineWidth(0)
        self.settings_toggle_1_layout_2 = QHBoxLayout(self.search_box_frame)
        self.settings_toggle_1_layout_2.setSpacing(0)
        self.settings_toggle_1_layout_2.setObjectName(u"settings_toggle_1_layout_2")
        self.settings_toggle_1_layout_2.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.search)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(120, 140, 891, 491))
        self.label_29.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_30 = QLabel(self.search)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(200, 190, 91, 71))
        self.label_30.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_31 = QLabel(self.search)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(200, 280, 91, 71))
        self.label_31.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_32 = QLabel(self.search)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(200, 360, 91, 71))
        self.label_32.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_33 = QLabel(self.search)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(200, 445, 91, 71))
        self.label_33.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_34 = QLabel(self.search)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(200, 530, 91, 71))
        self.label_34.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_35 = QLabel(self.search)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(320, 190, 450, 71))
        self.label_35.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_36 = QLabel(self.search)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(320, 280, 450, 71))
        self.label_36.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_37 = QLabel(self.search)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(320, 362, 450, 71))
        self.label_37.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_38 = QLabel(self.search)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(320, 445, 450, 71))
        self.label_38.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_39 = QLabel(self.search)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(320, 530, 450, 71))
        self.label_39.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_40 = QLabel(self.search)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(810, 190, 131, 71))
        self.label_40.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(194, 234, 189);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_41 = QLabel(self.search)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(810, 280, 131, 71))
        self.label_41.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(194, 234, 189);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_42 = QLabel(self.search)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(810, 360, 131, 71))
        self.label_42.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(194, 234, 189);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_43 = QLabel(self.search)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(810, 445, 131, 71))
        self.label_43.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(194, 234, 189);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_44 = QLabel(self.search)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(810, 530, 131, 71))
        self.label_44.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(194, 234, 189);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_7 = QLabel(self.search)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 160, 49, 16))
        font6 = QFont()
        font6.setPointSize(11)
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"")
        self.label_8 = QLabel(self.search)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 160, 91, 16))
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"")
        self.label_9 = QLabel(self.search)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(840, 163, 91, 16))
        self.label_9.setFont(font6)
        self.label_9.setStyleSheet(u"")
        self.label_45 = QLabel(self.search)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(690, 70, 91, 51))
        self.label_45.setCursor(QCursor(Qt.ArrowCursor))
        self.label_45.setStyleSheet(u"QLabel {\n"
"			\n"
"			background-color: rgb(214, 193, 157);\n"
"			padding: 12px;\n"
"			border-bottom-right-radius: 25px;\n"
"			border-top-right-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.app_desc_frame_1 = QFrame(self.search)
        self.app_desc_frame_1.setObjectName(u"app_desc_frame_1")
        self.app_desc_frame_1.setGeometry(QRect(320, 210, 391, 51))
        self.app_desc_frame_1.setStyleSheet(u"")
        self.app_desc_frame_1.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_1.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_1.setLineWidth(0)
        self.app_desc_1_layout = QHBoxLayout(self.app_desc_frame_1)
        self.app_desc_1_layout.setSpacing(0)
        self.app_desc_1_layout.setObjectName(u"app_desc_1_layout")
        self.app_desc_1_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_2 = QFrame(self.search)
        self.app_desc_frame_2.setObjectName(u"app_desc_frame_2")
        self.app_desc_frame_2.setGeometry(QRect(320, 290, 391, 51))
        self.app_desc_frame_2.setStyleSheet(u"")
        self.app_desc_frame_2.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_2.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_2.setLineWidth(0)
        self.app_desc_2_layout = QHBoxLayout(self.app_desc_frame_2)
        self.app_desc_2_layout.setSpacing(0)
        self.app_desc_2_layout.setObjectName(u"app_desc_2_layout")
        self.app_desc_2_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_3 = QFrame(self.search)
        self.app_desc_frame_3.setObjectName(u"app_desc_frame_3")
        self.app_desc_frame_3.setGeometry(QRect(320, 370, 391, 51))
        self.app_desc_frame_3.setStyleSheet(u"")
        self.app_desc_frame_3.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_3.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_3.setLineWidth(0)
        self.app_desc_3_layout = QHBoxLayout(self.app_desc_frame_3)
        self.app_desc_3_layout.setSpacing(0)
        self.app_desc_3_layout.setObjectName(u"app_desc_3_layout")
        self.app_desc_3_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_4 = QFrame(self.search)
        self.app_desc_frame_4.setObjectName(u"app_desc_frame_4")
        self.app_desc_frame_4.setGeometry(QRect(320, 460, 391, 51))
        self.app_desc_frame_4.setStyleSheet(u"")
        self.app_desc_frame_4.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_4.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_4.setLineWidth(0)
        self.app_desc_4_layout = QHBoxLayout(self.app_desc_frame_4)
        self.app_desc_4_layout.setSpacing(0)
        self.app_desc_4_layout.setObjectName(u"app_desc_4_layout")
        self.app_desc_4_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_5 = QFrame(self.search)
        self.app_desc_frame_5.setObjectName(u"app_desc_frame_5")
        self.app_desc_frame_5.setGeometry(QRect(320, 540, 391, 51))
        self.app_desc_frame_5.setStyleSheet(u"")
        self.app_desc_frame_5.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_5.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_5.setLineWidth(0)
        self.app_desc_5_layout = QHBoxLayout(self.app_desc_frame_5)
        self.app_desc_5_layout.setSpacing(0)
        self.app_desc_5_layout.setObjectName(u"app_desc_5_layout")
        self.app_desc_5_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_1 = QFrame(self.search)
        self.app_install_frame_1.setObjectName(u"app_install_frame_1")
        self.app_install_frame_1.setGeometry(QRect(820, 200, 101, 51))
        self.app_install_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_1.setStyleSheet(u"")
        self.app_install_frame_1.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_1.setFrameShadow(QFrame.Raised)
        self.app_install_frame_1.setLineWidth(0)
        self.app_install_1_layout = QHBoxLayout(self.app_install_frame_1)
        self.app_install_1_layout.setSpacing(0)
        self.app_install_1_layout.setObjectName(u"app_install_1_layout")
        self.app_install_1_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_2 = QFrame(self.search)
        self.app_install_frame_2.setObjectName(u"app_install_frame_2")
        self.app_install_frame_2.setGeometry(QRect(820, 290, 101, 51))
        self.app_install_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_2.setStyleSheet(u"")
        self.app_install_frame_2.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_2.setFrameShadow(QFrame.Raised)
        self.app_install_frame_2.setLineWidth(0)
        self.app_install_2_layout = QHBoxLayout(self.app_install_frame_2)
        self.app_install_2_layout.setSpacing(0)
        self.app_install_2_layout.setObjectName(u"app_install_2_layout")
        self.app_install_2_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_3 = QFrame(self.search)
        self.app_install_frame_3.setObjectName(u"app_install_frame_3")
        self.app_install_frame_3.setGeometry(QRect(820, 370, 101, 51))
        self.app_install_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_3.setStyleSheet(u"")
        self.app_install_frame_3.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_3.setFrameShadow(QFrame.Raised)
        self.app_install_frame_3.setLineWidth(0)
        self.app_install_3_layout = QHBoxLayout(self.app_install_frame_3)
        self.app_install_3_layout.setSpacing(0)
        self.app_install_3_layout.setObjectName(u"app_install_3_layout")
        self.app_install_3_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_4 = QFrame(self.search)
        self.app_install_frame_4.setObjectName(u"app_install_frame_4")
        self.app_install_frame_4.setGeometry(QRect(820, 450, 101, 51))
        self.app_install_frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_4.setStyleSheet(u"")
        self.app_install_frame_4.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_4.setFrameShadow(QFrame.Raised)
        self.app_install_frame_4.setLineWidth(0)
        self.app_install_4_layout = QHBoxLayout(self.app_install_frame_4)
        self.app_install_4_layout.setSpacing(0)
        self.app_install_4_layout.setObjectName(u"app_install_4_layout")
        self.app_install_4_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_5 = QFrame(self.search)
        self.app_install_frame_5.setObjectName(u"app_install_frame_5")
        self.app_install_frame_5.setGeometry(QRect(820, 540, 101, 51))
        self.app_install_frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_5.setStyleSheet(u"")
        self.app_install_frame_5.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_5.setFrameShadow(QFrame.Raised)
        self.app_install_frame_5.setLineWidth(0)
        self.app_install_5_layout = QHBoxLayout(self.app_install_frame_5)
        self.app_install_5_layout.setSpacing(0)
        self.app_install_5_layout.setObjectName(u"app_install_5_layout")
        self.app_install_5_layout.setContentsMargins(0, 0, 0, 0)
        self.app_search_frame = QFrame(self.search)
        self.app_search_frame.setObjectName(u"app_search_frame")
        self.app_search_frame.setGeometry(QRect(700, 80, 71, 31))
        self.app_search_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_search_frame.setStyleSheet(u"background-color: rgb(214, 193, 157);\n"
"")
        self.app_search_frame.setFrameShape(QFrame.NoFrame)
        self.app_search_frame.setFrameShadow(QFrame.Raised)
        self.app_search_frame.setLineWidth(0)
        self.app_search_layout_ = QHBoxLayout(self.app_search_frame)
        self.app_search_layout_.setSpacing(0)
        self.app_search_layout_.setObjectName(u"app_search_layout_")
        self.app_search_layout_.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.search)
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_27.raise_()
        self.search_box_frame.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_39.raise_()
        self.label_40.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.label_43.raise_()
        self.label_44.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.app_desc_frame_1.raise_()
        self.app_desc_frame_2.raise_()
        self.app_desc_frame_3.raise_()
        self.app_desc_frame_4.raise_()
        self.app_desc_frame_5.raise_()
        self.app_install_frame_1.raise_()
        self.label_9.raise_()
        self.app_install_frame_2.raise_()
        self.app_install_frame_3.raise_()
        self.app_install_frame_4.raise_()
        self.app_install_frame_5.raise_()
        self.label_45.raise_()
        self.app_search_frame.raise_()
        self.recommended_apps_page_2 = QWidget()
        self.recommended_apps_page_2.setObjectName(u"recommended_apps_page_2")
        self.label_58 = QLabel(self.recommended_apps_page_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(30, 50, 1071, 611))
        self.label_58.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_59 = QLabel(self.recommended_apps_page_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(80, 130, 891, 511))
        self.label_59.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_61 = QLabel(self.recommended_apps_page_2)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(280, 170, 450, 71))
        self.label_61.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_62 = QLabel(self.recommended_apps_page_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(160, 170, 91, 71))
        self.label_62.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_64 = QLabel(self.recommended_apps_page_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(280, 260, 450, 71))
        self.label_64.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_65 = QLabel(self.recommended_apps_page_2)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(160, 260, 91, 71))
        self.label_65.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_67 = QLabel(self.recommended_apps_page_2)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(280, 350, 450, 71))
        self.label_67.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_68 = QLabel(self.recommended_apps_page_2)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(160, 350, 91, 71))
        self.label_68.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_70 = QLabel(self.recommended_apps_page_2)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(280, 440, 450, 71))
        self.label_70.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_71 = QLabel(self.recommended_apps_page_2)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(160, 440, 91, 71))
        self.label_71.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_73 = QLabel(self.recommended_apps_page_2)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(280, 530, 450, 71))
        self.label_73.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_74 = QLabel(self.recommended_apps_page_2)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(160, 530, 91, 71))
        self.label_74.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_76 = QLabel(self.recommended_apps_page_2)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(180, 190, 71, 31))
        self.label_76.setFont(font6)
        self.label_76.setStyleSheet(u"")
        self.label_77 = QLabel(self.recommended_apps_page_2)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(300, 190, 411, 31))
        font7 = QFont()
        font7.setPointSize(8)
        self.label_77.setFont(font7)
        self.label_77.setStyleSheet(u"")
        self.label_77.setWordWrap(True)
        self.label_78 = QLabel(self.recommended_apps_page_2)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(170, 280, 71, 31))
        self.label_78.setFont(font6)
        self.label_78.setStyleSheet(u"")
        self.label_79 = QLabel(self.recommended_apps_page_2)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(300, 280, 411, 31))
        self.label_79.setFont(font7)
        self.label_79.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.label_79.setWordWrap(True)
        self.label_80 = QLabel(self.recommended_apps_page_2)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(170, 370, 71, 31))
        self.label_80.setFont(font6)
        self.label_80.setStyleSheet(u"")
        self.label_81 = QLabel(self.recommended_apps_page_2)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(300, 370, 411, 31))
        self.label_81.setFont(font7)
        self.label_81.setStyleSheet(u"")
        self.label_81.setWordWrap(True)
        self.label_82 = QLabel(self.recommended_apps_page_2)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(170, 450, 71, 51))
        self.label_82.setFont(font6)
        self.label_82.setStyleSheet(u"")
        self.label_82.setWordWrap(True)
        self.label_83 = QLabel(self.recommended_apps_page_2)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(290, 460, 411, 31))
        self.label_83.setFont(font7)
        self.label_83.setStyleSheet(u"")
        self.label_83.setWordWrap(True)
        self.label_84 = QLabel(self.recommended_apps_page_2)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(170, 540, 81, 51))
        self.label_84.setFont(font6)
        self.label_84.setStyleSheet(u"")
        self.label_84.setWordWrap(True)
        self.label_85 = QLabel(self.recommended_apps_page_2)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(290, 550, 411, 31))
        self.label_85.setFont(font7)
        self.label_85.setStyleSheet(u"")
        self.label_85.setWordWrap(True)
        self.recc_app_install_frame_6 = QFrame(self.recommended_apps_page_2)
        self.recc_app_install_frame_6.setObjectName(u"recc_app_install_frame_6")
        self.recc_app_install_frame_6.setGeometry(QRect(770, 170, 131, 71))
        self.recc_app_install_frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_6.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_6.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_6.setLineWidth(0)
        self.recc_app_install_layout_6 = QHBoxLayout(self.recc_app_install_frame_6)
        self.recc_app_install_layout_6.setSpacing(0)
        self.recc_app_install_layout_6.setObjectName(u"recc_app_install_layout_6")
        self.recc_app_install_layout_6.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_7 = QFrame(self.recommended_apps_page_2)
        self.recc_app_install_frame_7.setObjectName(u"recc_app_install_frame_7")
        self.recc_app_install_frame_7.setGeometry(QRect(770, 260, 131, 71))
        self.recc_app_install_frame_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_7.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_7.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_7.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_7.setLineWidth(0)
        self.recc_app_install_layout_7 = QHBoxLayout(self.recc_app_install_frame_7)
        self.recc_app_install_layout_7.setSpacing(0)
        self.recc_app_install_layout_7.setObjectName(u"recc_app_install_layout_7")
        self.recc_app_install_layout_7.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_8 = QFrame(self.recommended_apps_page_2)
        self.recc_app_install_frame_8.setObjectName(u"recc_app_install_frame_8")
        self.recc_app_install_frame_8.setGeometry(QRect(770, 350, 131, 71))
        self.recc_app_install_frame_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_8.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_8.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_8.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_8.setLineWidth(0)
        self.recc_app_install_layout_8 = QHBoxLayout(self.recc_app_install_frame_8)
        self.recc_app_install_layout_8.setSpacing(0)
        self.recc_app_install_layout_8.setObjectName(u"recc_app_install_layout_8")
        self.recc_app_install_layout_8.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_9 = QFrame(self.recommended_apps_page_2)
        self.recc_app_install_frame_9.setObjectName(u"recc_app_install_frame_9")
        self.recc_app_install_frame_9.setGeometry(QRect(770, 440, 131, 71))
        self.recc_app_install_frame_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_9.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_9.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_9.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_9.setLineWidth(0)
        self.recc_app_install_layout_9 = QHBoxLayout(self.recc_app_install_frame_9)
        self.recc_app_install_layout_9.setSpacing(0)
        self.recc_app_install_layout_9.setObjectName(u"recc_app_install_layout_9")
        self.recc_app_install_layout_9.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_10 = QFrame(self.recommended_apps_page_2)
        self.recc_app_install_frame_10.setObjectName(u"recc_app_install_frame_10")
        self.recc_app_install_frame_10.setGeometry(QRect(770, 530, 131, 71))
        self.recc_app_install_frame_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_10.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_10.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_10.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_10.setLineWidth(0)
        self.recc_app_install_layout_10 = QHBoxLayout(self.recc_app_install_frame_10)
        self.recc_app_install_layout_10.setSpacing(0)
        self.recc_app_install_layout_10.setObjectName(u"recc_app_install_layout_10")
        self.recc_app_install_layout_10.setContentsMargins(0, 0, 0, 0)
        self.label_172 = QLabel(self.recommended_apps_page_2)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(590, 80, 51, 31))
        self.label_172.setFont(font6)
        self.label_172.setStyleSheet(u"")
        self.title_8 = QLabel(self.recommended_apps_page_2)
        self.title_8.setObjectName(u"title_8")
        self.title_8.setGeometry(QRect(160, 75, 331, 41))
        font8 = QFont()
        font8.setPointSize(13)
        self.title_8.setFont(font8)
        self.title_8.setStyleSheet(u"")
        self.title_8.setAlignment(Qt.AlignCenter)
        self.label_173 = QLabel(self.recommended_apps_page_2)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(110, 70, 441, 51))
        self.label_173.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_174 = QLabel(self.recommended_apps_page_2)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(580, 70, 361, 51))
        self.label_174.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.status_indicator_frame_2 = QFrame(self.recommended_apps_page_2)
        self.status_indicator_frame_2.setObjectName(u"status_indicator_frame_2")
        self.status_indicator_frame_2.setGeometry(QRect(640, 70, 281, 51))
        self.status_indicator_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_indicator_frame_2.setStyleSheet(u"")
        self.status_indicator_frame_2.setFrameShape(QFrame.NoFrame)
        self.status_indicator_frame_2.setFrameShadow(QFrame.Raised)
        self.status_indicator_frame_2.setLineWidth(0)
        self.status_indicator_layout_2 = QHBoxLayout(self.status_indicator_frame_2)
        self.status_indicator_layout_2.setSpacing(0)
        self.status_indicator_layout_2.setObjectName(u"status_indicator_layout_2")
        self.status_indicator_layout_2.setContentsMargins(0, 0, 0, 0)
        self.label_331 = QLabel(self.recommended_apps_page_2)
        self.label_331.setObjectName(u"label_331")
        self.label_331.setGeometry(QRect(1000, 140, 71, 201))
        self.label_331.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.back_button_frame_5 = QFrame(self.recommended_apps_page_2)
        self.back_button_frame_5.setObjectName(u"back_button_frame_5")
        self.back_button_frame_5.setGeometry(QRect(1010, 150, 51, 181))
        self.back_button_frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_5.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_5.setFrameShadow(QFrame.Raised)
        self.back_button_frame_5.setLineWidth(0)
        self.return_home_layout_two = QHBoxLayout(self.back_button_frame_5)
        self.return_home_layout_two.setSpacing(0)
        self.return_home_layout_two.setObjectName(u"return_home_layout_two")
        self.return_home_layout_two.setContentsMargins(0, 0, 0, 0)
        self.label_332 = QLabel(self.recommended_apps_page_2)
        self.label_332.setObjectName(u"label_332")
        self.label_332.setGeometry(QRect(1000, 350, 71, 281))
        self.label_332.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_333 = QLabel(self.recommended_apps_page_2)
        self.label_333.setObjectName(u"label_333")
        self.label_333.setGeometry(QRect(980, 130, 111, 511))
        self.label_333.setStyleSheet(u"QLabel {\n"
"        	\n"
"			\n"
"	background-color: rgb(212, 212, 212);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.recc_next_page_frame_3 = QFrame(self.recommended_apps_page_2)
        self.recc_next_page_frame_3.setObjectName(u"recc_next_page_frame_3")
        self.recc_next_page_frame_3.setGeometry(QRect(1010, 360, 51, 261))
        self.recc_next_page_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_next_page_frame_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_next_page_frame_3.setFrameShape(QFrame.NoFrame)
        self.recc_next_page_frame_3.setFrameShadow(QFrame.Raised)
        self.recc_next_page_frame_3.setLineWidth(0)
        self.recc_next_page_layout_two = QHBoxLayout(self.recc_next_page_frame_3)
        self.recc_next_page_layout_two.setSpacing(0)
        self.recc_next_page_layout_two.setObjectName(u"recc_next_page_layout_two")
        self.recc_next_page_layout_two.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.recommended_apps_page_2)
        self.label_58.raise_()
        self.label_333.raise_()
        self.label_59.raise_()
        self.label_61.raise_()
        self.label_62.raise_()
        self.label_64.raise_()
        self.label_65.raise_()
        self.label_67.raise_()
        self.label_68.raise_()
        self.label_70.raise_()
        self.label_71.raise_()
        self.label_73.raise_()
        self.label_74.raise_()
        self.label_76.raise_()
        self.label_77.raise_()
        self.label_78.raise_()
        self.label_79.raise_()
        self.label_80.raise_()
        self.label_81.raise_()
        self.label_82.raise_()
        self.label_83.raise_()
        self.label_84.raise_()
        self.label_85.raise_()
        self.recc_app_install_frame_6.raise_()
        self.recc_app_install_frame_7.raise_()
        self.recc_app_install_frame_8.raise_()
        self.recc_app_install_frame_9.raise_()
        self.recc_app_install_frame_10.raise_()
        self.label_173.raise_()
        self.label_174.raise_()
        self.status_indicator_frame_2.raise_()
        self.label_172.raise_()
        self.title_8.raise_()
        self.label_331.raise_()
        self.label_332.raise_()
        self.recc_next_page_frame_3.raise_()
        self.back_button_frame_5.raise_()
        self.recommended_apps_page_3 = QWidget()
        self.recommended_apps_page_3.setObjectName(u"recommended_apps_page_3")
        self.label_114 = QLabel(self.recommended_apps_page_3)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(280, 260, 450, 71))
        self.label_114.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_115 = QLabel(self.recommended_apps_page_3)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(280, 350, 450, 71))
        self.label_115.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_116 = QLabel(self.recommended_apps_page_3)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(170, 280, 71, 31))
        self.label_116.setFont(font6)
        self.label_116.setStyleSheet(u"")
        self.label_118 = QLabel(self.recommended_apps_page_3)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(300, 370, 411, 31))
        self.label_118.setFont(font7)
        self.label_118.setStyleSheet(u"")
        self.label_118.setWordWrap(True)
        self.label_119 = QLabel(self.recommended_apps_page_3)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(160, 530, 91, 71))
        self.label_119.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_120 = QLabel(self.recommended_apps_page_3)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(170, 180, 71, 51))
        self.label_120.setFont(font6)
        self.label_120.setStyleSheet(u"")
        self.label_120.setWordWrap(True)
        self.label_121 = QLabel(self.recommended_apps_page_3)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(290, 550, 411, 31))
        self.label_121.setFont(font7)
        self.label_121.setStyleSheet(u"")
        self.label_121.setWordWrap(True)
        self.label_122 = QLabel(self.recommended_apps_page_3)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(280, 530, 450, 71))
        self.label_122.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_124 = QLabel(self.recommended_apps_page_3)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(30, 50, 1071, 611))
        self.label_124.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_125 = QLabel(self.recommended_apps_page_3)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(290, 460, 411, 31))
        self.label_125.setFont(font7)
        self.label_125.setStyleSheet(u"")
        self.label_125.setWordWrap(True)
        self.label_126 = QLabel(self.recommended_apps_page_3)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(80, 130, 891, 511))
        self.label_126.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_128 = QLabel(self.recommended_apps_page_3)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(300, 190, 411, 31))
        self.label_128.setFont(font7)
        self.label_128.setStyleSheet(u"")
        self.label_128.setWordWrap(True)
        self.label_130 = QLabel(self.recommended_apps_page_3)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(160, 170, 91, 71))
        self.label_130.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_131 = QLabel(self.recommended_apps_page_3)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(170, 360, 71, 51))
        self.label_131.setFont(font6)
        self.label_131.setStyleSheet(u"")
        self.label_131.setWordWrap(True)
        self.label_132 = QLabel(self.recommended_apps_page_3)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(170, 450, 71, 51))
        self.label_132.setFont(font6)
        self.label_132.setStyleSheet(u"")
        self.label_132.setWordWrap(True)
        self.label_133 = QLabel(self.recommended_apps_page_3)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(280, 440, 450, 71))
        self.label_133.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_134 = QLabel(self.recommended_apps_page_3)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(280, 170, 450, 71))
        self.label_134.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_136 = QLabel(self.recommended_apps_page_3)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(170, 540, 81, 51))
        self.label_136.setFont(font6)
        self.label_136.setStyleSheet(u"")
        self.label_136.setWordWrap(True)
        self.label_137 = QLabel(self.recommended_apps_page_3)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(160, 350, 91, 71))
        self.label_137.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_138 = QLabel(self.recommended_apps_page_3)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(160, 440, 91, 71))
        self.label_138.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_140 = QLabel(self.recommended_apps_page_3)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(160, 260, 91, 71))
        self.label_140.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_141 = QLabel(self.recommended_apps_page_3)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(300, 280, 411, 31))
        self.label_141.setFont(font7)
        self.label_141.setStyleSheet(u"")
        self.label_141.setWordWrap(True)
        self.recc_app_install_frame_11 = QFrame(self.recommended_apps_page_3)
        self.recc_app_install_frame_11.setObjectName(u"recc_app_install_frame_11")
        self.recc_app_install_frame_11.setGeometry(QRect(770, 170, 131, 71))
        self.recc_app_install_frame_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_11.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_11.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_11.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_11.setLineWidth(0)
        self.recc_app_install_layout_11 = QHBoxLayout(self.recc_app_install_frame_11)
        self.recc_app_install_layout_11.setSpacing(0)
        self.recc_app_install_layout_11.setObjectName(u"recc_app_install_layout_11")
        self.recc_app_install_layout_11.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_12 = QFrame(self.recommended_apps_page_3)
        self.recc_app_install_frame_12.setObjectName(u"recc_app_install_frame_12")
        self.recc_app_install_frame_12.setGeometry(QRect(770, 260, 131, 71))
        self.recc_app_install_frame_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_12.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_12.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_12.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_12.setLineWidth(0)
        self.recc_app_install_layout_12 = QHBoxLayout(self.recc_app_install_frame_12)
        self.recc_app_install_layout_12.setSpacing(0)
        self.recc_app_install_layout_12.setObjectName(u"recc_app_install_layout_12")
        self.recc_app_install_layout_12.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_13 = QFrame(self.recommended_apps_page_3)
        self.recc_app_install_frame_13.setObjectName(u"recc_app_install_frame_13")
        self.recc_app_install_frame_13.setGeometry(QRect(770, 350, 131, 71))
        self.recc_app_install_frame_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_13.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_13.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_13.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_13.setLineWidth(0)
        self.recc_app_install_layout_13 = QHBoxLayout(self.recc_app_install_frame_13)
        self.recc_app_install_layout_13.setSpacing(0)
        self.recc_app_install_layout_13.setObjectName(u"recc_app_install_layout_13")
        self.recc_app_install_layout_13.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_14 = QFrame(self.recommended_apps_page_3)
        self.recc_app_install_frame_14.setObjectName(u"recc_app_install_frame_14")
        self.recc_app_install_frame_14.setGeometry(QRect(770, 440, 131, 71))
        self.recc_app_install_frame_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_14.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_14.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_14.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_14.setLineWidth(0)
        self.recc_app_install_layout_14 = QHBoxLayout(self.recc_app_install_frame_14)
        self.recc_app_install_layout_14.setSpacing(0)
        self.recc_app_install_layout_14.setObjectName(u"recc_app_install_layout_14")
        self.recc_app_install_layout_14.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_15 = QFrame(self.recommended_apps_page_3)
        self.recc_app_install_frame_15.setObjectName(u"recc_app_install_frame_15")
        self.recc_app_install_frame_15.setGeometry(QRect(770, 530, 131, 71))
        self.recc_app_install_frame_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_15.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_15.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_15.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_15.setLineWidth(0)
        self.recc_app_install_layout_15 = QHBoxLayout(self.recc_app_install_frame_15)
        self.recc_app_install_layout_15.setSpacing(0)
        self.recc_app_install_layout_15.setObjectName(u"recc_app_install_layout_15")
        self.recc_app_install_layout_15.setContentsMargins(0, 0, 0, 0)
        self.label_175 = QLabel(self.recommended_apps_page_3)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setGeometry(QRect(590, 75, 51, 31))
        self.label_175.setFont(font6)
        self.label_175.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.title_9 = QLabel(self.recommended_apps_page_3)
        self.title_9.setObjectName(u"title_9")
        self.title_9.setGeometry(QRect(160, 70, 331, 41))
        self.title_9.setFont(font8)
        self.title_9.setStyleSheet(u"")
        self.title_9.setAlignment(Qt.AlignCenter)
        self.status_indicator_frame_3 = QFrame(self.recommended_apps_page_3)
        self.status_indicator_frame_3.setObjectName(u"status_indicator_frame_3")
        self.status_indicator_frame_3.setGeometry(QRect(640, 65, 281, 51))
        self.status_indicator_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_indicator_frame_3.setStyleSheet(u"")
        self.status_indicator_frame_3.setFrameShape(QFrame.NoFrame)
        self.status_indicator_frame_3.setFrameShadow(QFrame.Raised)
        self.status_indicator_frame_3.setLineWidth(0)
        self.status_indicator_layout_3 = QHBoxLayout(self.status_indicator_frame_3)
        self.status_indicator_layout_3.setSpacing(0)
        self.status_indicator_layout_3.setObjectName(u"status_indicator_layout_3")
        self.status_indicator_layout_3.setContentsMargins(0, 0, 0, 0)
        self.label_176 = QLabel(self.recommended_apps_page_3)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setGeometry(QRect(110, 65, 441, 51))
        self.label_176.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_177 = QLabel(self.recommended_apps_page_3)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setGeometry(QRect(580, 65, 361, 51))
        self.label_177.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.recc_next_page_frame_4 = QFrame(self.recommended_apps_page_3)
        self.recc_next_page_frame_4.setObjectName(u"recc_next_page_frame_4")
        self.recc_next_page_frame_4.setGeometry(QRect(1010, 360, 51, 261))
        self.recc_next_page_frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_next_page_frame_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_next_page_frame_4.setFrameShape(QFrame.NoFrame)
        self.recc_next_page_frame_4.setFrameShadow(QFrame.Raised)
        self.recc_next_page_frame_4.setLineWidth(0)
        self.recc_next_page_layout_3 = QHBoxLayout(self.recc_next_page_frame_4)
        self.recc_next_page_layout_3.setSpacing(0)
        self.recc_next_page_layout_3.setObjectName(u"recc_next_page_layout_3")
        self.recc_next_page_layout_3.setContentsMargins(0, 0, 0, 0)
        self.label_334 = QLabel(self.recommended_apps_page_3)
        self.label_334.setObjectName(u"label_334")
        self.label_334.setGeometry(QRect(980, 130, 111, 511))
        self.label_334.setStyleSheet(u"QLabel {\n"
"        	\n"
"			\n"
"	background-color: rgb(212, 212, 212);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_335 = QLabel(self.recommended_apps_page_3)
        self.label_335.setObjectName(u"label_335")
        self.label_335.setGeometry(QRect(1000, 140, 71, 201))
        self.label_335.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.back_button_frame_6 = QFrame(self.recommended_apps_page_3)
        self.back_button_frame_6.setObjectName(u"back_button_frame_6")
        self.back_button_frame_6.setGeometry(QRect(1010, 150, 51, 181))
        self.back_button_frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_6.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_6.setFrameShadow(QFrame.Raised)
        self.back_button_frame_6.setLineWidth(0)
        self.return_home_layout_3 = QHBoxLayout(self.back_button_frame_6)
        self.return_home_layout_3.setSpacing(0)
        self.return_home_layout_3.setObjectName(u"return_home_layout_3")
        self.return_home_layout_3.setContentsMargins(0, 0, 0, 0)
        self.label_336 = QLabel(self.recommended_apps_page_3)
        self.label_336.setObjectName(u"label_336")
        self.label_336.setGeometry(QRect(1000, 350, 71, 281))
        self.label_336.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.stackedWidget.addWidget(self.recommended_apps_page_3)
        self.label_124.raise_()
        self.label_334.raise_()
        self.label_126.raise_()
        self.label_130.raise_()
        self.label_133.raise_()
        self.label_134.raise_()
        self.label_137.raise_()
        self.label_138.raise_()
        self.label_140.raise_()
        self.label_114.raise_()
        self.label_115.raise_()
        self.label_116.raise_()
        self.label_118.raise_()
        self.label_119.raise_()
        self.label_120.raise_()
        self.label_122.raise_()
        self.label_121.raise_()
        self.label_125.raise_()
        self.label_128.raise_()
        self.label_131.raise_()
        self.label_132.raise_()
        self.label_136.raise_()
        self.label_141.raise_()
        self.recc_app_install_frame_11.raise_()
        self.recc_app_install_frame_12.raise_()
        self.recc_app_install_frame_13.raise_()
        self.recc_app_install_frame_14.raise_()
        self.recc_app_install_frame_15.raise_()
        self.label_176.raise_()
        self.label_177.raise_()
        self.title_9.raise_()
        self.label_175.raise_()
        self.status_indicator_frame_3.raise_()
        self.label_335.raise_()
        self.label_336.raise_()
        self.recc_next_page_frame_4.raise_()
        self.back_button_frame_6.raise_()
        self.recommended_apps_page_4 = QWidget()
        self.recommended_apps_page_4.setObjectName(u"recommended_apps_page_4")
        self.label_142 = QLabel(self.recommended_apps_page_4)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setGeometry(QRect(280, 260, 450, 71))
        self.label_142.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_143 = QLabel(self.recommended_apps_page_4)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(280, 350, 450, 71))
        self.label_143.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_144 = QLabel(self.recommended_apps_page_4)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setGeometry(QRect(170, 280, 71, 31))
        self.label_144.setFont(font6)
        self.label_144.setStyleSheet(u"")
        self.label_146 = QLabel(self.recommended_apps_page_4)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(300, 370, 411, 31))
        self.label_146.setFont(font7)
        self.label_146.setStyleSheet(u"")
        self.label_146.setWordWrap(True)
        self.label_147 = QLabel(self.recommended_apps_page_4)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setGeometry(QRect(160, 530, 91, 71))
        self.label_147.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_148 = QLabel(self.recommended_apps_page_4)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setGeometry(QRect(170, 190, 71, 31))
        self.label_148.setFont(font6)
        self.label_148.setStyleSheet(u"")
        self.label_149 = QLabel(self.recommended_apps_page_4)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setGeometry(QRect(290, 550, 411, 31))
        self.label_149.setFont(font7)
        self.label_149.setStyleSheet(u"")
        self.label_149.setWordWrap(True)
        self.label_150 = QLabel(self.recommended_apps_page_4)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setGeometry(QRect(280, 530, 450, 71))
        self.label_150.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_152 = QLabel(self.recommended_apps_page_4)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setGeometry(QRect(30, 50, 1071, 611))
        self.label_152.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_153 = QLabel(self.recommended_apps_page_4)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(290, 460, 411, 31))
        self.label_153.setFont(font7)
        self.label_153.setStyleSheet(u"")
        self.label_153.setWordWrap(True)
        self.label_154 = QLabel(self.recommended_apps_page_4)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setGeometry(QRect(80, 130, 891, 511))
        self.label_154.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_156 = QLabel(self.recommended_apps_page_4)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setGeometry(QRect(300, 190, 411, 31))
        self.label_156.setFont(font7)
        self.label_156.setStyleSheet(u"")
        self.label_156.setWordWrap(True)
        self.label_158 = QLabel(self.recommended_apps_page_4)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setGeometry(QRect(160, 170, 91, 71))
        self.label_158.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_159 = QLabel(self.recommended_apps_page_4)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setGeometry(QRect(170, 370, 71, 31))
        self.label_159.setFont(font6)
        self.label_159.setStyleSheet(u"")
        self.label_160 = QLabel(self.recommended_apps_page_4)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(170, 450, 71, 51))
        self.label_160.setFont(font6)
        self.label_160.setStyleSheet(u"")
        self.label_160.setWordWrap(True)
        self.label_161 = QLabel(self.recommended_apps_page_4)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(280, 440, 450, 71))
        self.label_161.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_162 = QLabel(self.recommended_apps_page_4)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(280, 170, 450, 71))
        self.label_162.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_164 = QLabel(self.recommended_apps_page_4)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(170, 540, 71, 51))
        self.label_164.setFont(font6)
        self.label_164.setStyleSheet(u"")
        self.label_164.setWordWrap(True)
        self.label_165 = QLabel(self.recommended_apps_page_4)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(160, 350, 91, 71))
        self.label_165.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_166 = QLabel(self.recommended_apps_page_4)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(160, 440, 91, 71))
        self.label_166.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_168 = QLabel(self.recommended_apps_page_4)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(160, 260, 91, 71))
        self.label_168.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_169 = QLabel(self.recommended_apps_page_4)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(300, 280, 411, 31))
        self.label_169.setFont(font7)
        self.label_169.setStyleSheet(u"")
        self.label_169.setWordWrap(True)
        self.recc_app_install_frame_16 = QFrame(self.recommended_apps_page_4)
        self.recc_app_install_frame_16.setObjectName(u"recc_app_install_frame_16")
        self.recc_app_install_frame_16.setGeometry(QRect(770, 170, 131, 71))
        self.recc_app_install_frame_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_16.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_16.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_16.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_16.setLineWidth(0)
        self.recc_app_install_layout_16 = QHBoxLayout(self.recc_app_install_frame_16)
        self.recc_app_install_layout_16.setSpacing(0)
        self.recc_app_install_layout_16.setObjectName(u"recc_app_install_layout_16")
        self.recc_app_install_layout_16.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_17 = QFrame(self.recommended_apps_page_4)
        self.recc_app_install_frame_17.setObjectName(u"recc_app_install_frame_17")
        self.recc_app_install_frame_17.setGeometry(QRect(770, 260, 131, 71))
        self.recc_app_install_frame_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_17.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_17.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_17.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_17.setLineWidth(0)
        self.recc_app_install_layout_17 = QHBoxLayout(self.recc_app_install_frame_17)
        self.recc_app_install_layout_17.setSpacing(0)
        self.recc_app_install_layout_17.setObjectName(u"recc_app_install_layout_17")
        self.recc_app_install_layout_17.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_18 = QFrame(self.recommended_apps_page_4)
        self.recc_app_install_frame_18.setObjectName(u"recc_app_install_frame_18")
        self.recc_app_install_frame_18.setGeometry(QRect(770, 350, 131, 71))
        self.recc_app_install_frame_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_18.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_18.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_18.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_18.setLineWidth(0)
        self.recc_app_install_layout_18 = QHBoxLayout(self.recc_app_install_frame_18)
        self.recc_app_install_layout_18.setSpacing(0)
        self.recc_app_install_layout_18.setObjectName(u"recc_app_install_layout_18")
        self.recc_app_install_layout_18.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_19 = QFrame(self.recommended_apps_page_4)
        self.recc_app_install_frame_19.setObjectName(u"recc_app_install_frame_19")
        self.recc_app_install_frame_19.setGeometry(QRect(770, 440, 131, 71))
        self.recc_app_install_frame_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_19.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_19.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_19.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_19.setLineWidth(0)
        self.recc_app_install_layout_19 = QHBoxLayout(self.recc_app_install_frame_19)
        self.recc_app_install_layout_19.setSpacing(0)
        self.recc_app_install_layout_19.setObjectName(u"recc_app_install_layout_19")
        self.recc_app_install_layout_19.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_20 = QFrame(self.recommended_apps_page_4)
        self.recc_app_install_frame_20.setObjectName(u"recc_app_install_frame_20")
        self.recc_app_install_frame_20.setGeometry(QRect(770, 530, 131, 71))
        self.recc_app_install_frame_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_20.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_20.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_20.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_20.setLineWidth(0)
        self.recc_app_install_layout_20 = QHBoxLayout(self.recc_app_install_frame_20)
        self.recc_app_install_layout_20.setSpacing(0)
        self.recc_app_install_layout_20.setObjectName(u"recc_app_install_layout_20")
        self.recc_app_install_layout_20.setContentsMargins(0, 0, 0, 0)
        self.label_178 = QLabel(self.recommended_apps_page_4)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(590, 80, 51, 31))
        self.label_178.setFont(font6)
        self.label_178.setStyleSheet(u"")
        self.status_indicator_frame_4 = QFrame(self.recommended_apps_page_4)
        self.status_indicator_frame_4.setObjectName(u"status_indicator_frame_4")
        self.status_indicator_frame_4.setGeometry(QRect(640, 70, 281, 51))
        self.status_indicator_frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_indicator_frame_4.setStyleSheet(u"")
        self.status_indicator_frame_4.setFrameShape(QFrame.NoFrame)
        self.status_indicator_frame_4.setFrameShadow(QFrame.Raised)
        self.status_indicator_frame_4.setLineWidth(0)
        self.status_indicator_layout_4 = QHBoxLayout(self.status_indicator_frame_4)
        self.status_indicator_layout_4.setSpacing(0)
        self.status_indicator_layout_4.setObjectName(u"status_indicator_layout_4")
        self.status_indicator_layout_4.setContentsMargins(0, 0, 0, 0)
        self.label_179 = QLabel(self.recommended_apps_page_4)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setGeometry(QRect(110, 70, 441, 51))
        self.label_179.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.title_10 = QLabel(self.recommended_apps_page_4)
        self.title_10.setObjectName(u"title_10")
        self.title_10.setGeometry(QRect(160, 75, 331, 41))
        self.title_10.setFont(font8)
        self.title_10.setStyleSheet(u"")
        self.title_10.setAlignment(Qt.AlignCenter)
        self.label_180 = QLabel(self.recommended_apps_page_4)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setGeometry(QRect(580, 70, 361, 51))
        self.label_180.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.recc_next_page_frame_5 = QFrame(self.recommended_apps_page_4)
        self.recc_next_page_frame_5.setObjectName(u"recc_next_page_frame_5")
        self.recc_next_page_frame_5.setGeometry(QRect(1010, 360, 51, 261))
        self.recc_next_page_frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_next_page_frame_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_next_page_frame_5.setFrameShape(QFrame.NoFrame)
        self.recc_next_page_frame_5.setFrameShadow(QFrame.Raised)
        self.recc_next_page_frame_5.setLineWidth(0)
        self.recc_next_page_layout_4 = QHBoxLayout(self.recc_next_page_frame_5)
        self.recc_next_page_layout_4.setSpacing(0)
        self.recc_next_page_layout_4.setObjectName(u"recc_next_page_layout_4")
        self.recc_next_page_layout_4.setContentsMargins(0, 0, 0, 0)
        self.label_337 = QLabel(self.recommended_apps_page_4)
        self.label_337.setObjectName(u"label_337")
        self.label_337.setGeometry(QRect(980, 130, 111, 511))
        self.label_337.setStyleSheet(u"QLabel {\n"
"        	\n"
"			\n"
"	background-color: rgb(212, 212, 212);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_338 = QLabel(self.recommended_apps_page_4)
        self.label_338.setObjectName(u"label_338")
        self.label_338.setGeometry(QRect(1000, 140, 71, 201))
        self.label_338.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.back_button_frame_7 = QFrame(self.recommended_apps_page_4)
        self.back_button_frame_7.setObjectName(u"back_button_frame_7")
        self.back_button_frame_7.setGeometry(QRect(1010, 150, 51, 181))
        self.back_button_frame_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_7.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_7.setFrameShadow(QFrame.Raised)
        self.back_button_frame_7.setLineWidth(0)
        self.return_home_layout_4 = QHBoxLayout(self.back_button_frame_7)
        self.return_home_layout_4.setSpacing(0)
        self.return_home_layout_4.setObjectName(u"return_home_layout_4")
        self.return_home_layout_4.setContentsMargins(0, 0, 0, 0)
        self.label_339 = QLabel(self.recommended_apps_page_4)
        self.label_339.setObjectName(u"label_339")
        self.label_339.setGeometry(QRect(1000, 350, 71, 281))
        self.label_339.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.stackedWidget.addWidget(self.recommended_apps_page_4)
        self.label_152.raise_()
        self.label_337.raise_()
        self.label_339.raise_()
        self.label_154.raise_()
        self.label_158.raise_()
        self.label_161.raise_()
        self.label_162.raise_()
        self.label_165.raise_()
        self.label_166.raise_()
        self.label_168.raise_()
        self.label_160.raise_()
        self.label_159.raise_()
        self.label_156.raise_()
        self.label_153.raise_()
        self.label_150.raise_()
        self.label_149.raise_()
        self.label_148.raise_()
        self.label_147.raise_()
        self.label_144.raise_()
        self.label_143.raise_()
        self.label_146.raise_()
        self.label_142.raise_()
        self.label_169.raise_()
        self.label_164.raise_()
        self.recc_app_install_frame_16.raise_()
        self.recc_app_install_frame_17.raise_()
        self.recc_app_install_frame_18.raise_()
        self.recc_app_install_frame_19.raise_()
        self.recc_app_install_frame_20.raise_()
        self.label_179.raise_()
        self.title_10.raise_()
        self.label_180.raise_()
        self.status_indicator_frame_4.raise_()
        self.label_178.raise_()
        self.recc_next_page_frame_5.raise_()
        self.label_338.raise_()
        self.back_button_frame_7.raise_()
        self.recommended_apps_page_5 = QWidget()
        self.recommended_apps_page_5.setObjectName(u"recommended_apps_page_5")
        self.recc_app_install_frame_21 = QFrame(self.recommended_apps_page_5)
        self.recc_app_install_frame_21.setObjectName(u"recc_app_install_frame_21")
        self.recc_app_install_frame_21.setGeometry(QRect(770, 440, 131, 71))
        self.recc_app_install_frame_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_21.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_21.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_21.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_21.setLineWidth(0)
        self.recc_app_install_layout_1_24 = QHBoxLayout(self.recc_app_install_frame_21)
        self.recc_app_install_layout_1_24.setSpacing(0)
        self.recc_app_install_layout_1_24.setObjectName(u"recc_app_install_layout_1_24")
        self.recc_app_install_layout_1_24.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.recommended_apps_page_5)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(300, 280, 411, 31))
        self.label_117.setFont(font7)
        self.label_117.setStyleSheet(u"")
        self.label_117.setWordWrap(True)
        self.label_95 = QLabel(self.recommended_apps_page_5)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(300, 370, 411, 31))
        self.label_95.setFont(font7)
        self.label_95.setStyleSheet(u"")
        self.label_95.setWordWrap(True)
        self.label_123 = QLabel(self.recommended_apps_page_5)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(80, 130, 891, 511))
        self.label_123.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_181 = QLabel(self.recommended_apps_page_5)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setGeometry(QRect(610, 70, 51, 31))
        self.label_181.setFont(font6)
        self.label_181.setStyleSheet(u"")
        self.label_127 = QLabel(self.recommended_apps_page_5)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(170, 370, 71, 31))
        self.label_127.setFont(font6)
        self.label_127.setStyleSheet(u"")
        self.recc_app_install_frame_22 = QFrame(self.recommended_apps_page_5)
        self.recc_app_install_frame_22.setObjectName(u"recc_app_install_frame_22")
        self.recc_app_install_frame_22.setGeometry(QRect(770, 530, 131, 71))
        self.recc_app_install_frame_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_22.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_22.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_22.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_22.setLineWidth(0)
        self.recc_app_install_layout_1_25 = QHBoxLayout(self.recc_app_install_frame_22)
        self.recc_app_install_layout_1_25.setSpacing(0)
        self.recc_app_install_layout_1_25.setObjectName(u"recc_app_install_layout_1_25")
        self.recc_app_install_layout_1_25.setContentsMargins(0, 0, 0, 0)
        self.label_129 = QLabel(self.recommended_apps_page_5)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(160, 350, 91, 71))
        self.label_129.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_135 = QLabel(self.recommended_apps_page_5)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(280, 170, 450, 71))
        self.label_135.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_139 = QLabel(self.recommended_apps_page_5)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(980, 130, 111, 511))
        self.label_139.setStyleSheet(u"QLabel {\n"
"        	\n"
"			\n"
"	background-color: rgb(212, 212, 212);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_145 = QLabel(self.recommended_apps_page_5)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(1000, 140, 71, 201))
        self.label_145.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_151 = QLabel(self.recommended_apps_page_5)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setGeometry(QRect(290, 530, 411, 31))
        self.label_151.setFont(font7)
        self.label_151.setStyleSheet(u"")
        self.label_151.setWordWrap(True)
        self.label_155 = QLabel(self.recommended_apps_page_5)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setGeometry(QRect(170, 180, 71, 51))
        self.label_155.setFont(font6)
        self.label_155.setStyleSheet(u"")
        self.label_155.setWordWrap(True)
        self.label_157 = QLabel(self.recommended_apps_page_5)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(30, 50, 1071, 621))
        self.label_157.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.status_indicator_frame_5 = QFrame(self.recommended_apps_page_5)
        self.status_indicator_frame_5.setObjectName(u"status_indicator_frame_5")
        self.status_indicator_frame_5.setGeometry(QRect(660, 60, 281, 51))
        self.status_indicator_frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_indicator_frame_5.setStyleSheet(u"")
        self.status_indicator_frame_5.setFrameShape(QFrame.NoFrame)
        self.status_indicator_frame_5.setFrameShadow(QFrame.Raised)
        self.status_indicator_frame_5.setLineWidth(0)
        self.status_indicator_layout_5 = QHBoxLayout(self.status_indicator_frame_5)
        self.status_indicator_layout_5.setSpacing(0)
        self.status_indicator_layout_5.setObjectName(u"status_indicator_layout_5")
        self.status_indicator_layout_5.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_23 = QFrame(self.recommended_apps_page_5)
        self.recc_app_install_frame_23.setObjectName(u"recc_app_install_frame_23")
        self.recc_app_install_frame_23.setGeometry(QRect(770, 170, 131, 71))
        self.recc_app_install_frame_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_23.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_23.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_23.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_23.setLineWidth(0)
        self.recc_app_install_layout_1_21 = QHBoxLayout(self.recc_app_install_frame_23)
        self.recc_app_install_layout_1_21.setSpacing(0)
        self.recc_app_install_layout_1_21.setObjectName(u"recc_app_install_layout_1_21")
        self.recc_app_install_layout_1_21.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_24 = QFrame(self.recommended_apps_page_5)
        self.recc_app_install_frame_24.setObjectName(u"recc_app_install_frame_24")
        self.recc_app_install_frame_24.setGeometry(QRect(770, 350, 131, 71))
        self.recc_app_install_frame_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_24.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_24.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_24.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_24.setLineWidth(0)
        self.recc_app_install_layout_1_23 = QHBoxLayout(self.recc_app_install_frame_24)
        self.recc_app_install_layout_1_23.setSpacing(0)
        self.recc_app_install_layout_1_23.setObjectName(u"recc_app_install_layout_1_23")
        self.recc_app_install_layout_1_23.setContentsMargins(0, 0, 0, 0)
        self.title_7 = QLabel(self.recommended_apps_page_5)
        self.title_7.setObjectName(u"title_7")
        self.title_7.setGeometry(QRect(180, 65, 331, 41))
        self.title_7.setFont(font8)
        self.title_7.setStyleSheet(u"")
        self.title_7.setAlignment(Qt.AlignCenter)
        self.label_163 = QLabel(self.recommended_apps_page_5)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(160, 530, 91, 81))
        self.label_163.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_167 = QLabel(self.recommended_apps_page_5)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(180, 540, 51, 61))
        self.label_167.setFont(font6)
        self.label_167.setStyleSheet(u"")
        self.label_167.setWordWrap(True)
        self.label_182 = QLabel(self.recommended_apps_page_5)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(280, 440, 450, 71))
        self.label_182.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.back_button_frame_3 = QFrame(self.recommended_apps_page_5)
        self.back_button_frame_3.setObjectName(u"back_button_frame_3")
        self.back_button_frame_3.setGeometry(QRect(1010, 150, 51, 181))
        self.back_button_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_3.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_3.setFrameShadow(QFrame.Raised)
        self.back_button_frame_3.setLineWidth(0)
        self.return_home_layout_5 = QHBoxLayout(self.back_button_frame_3)
        self.return_home_layout_5.setSpacing(0)
        self.return_home_layout_5.setObjectName(u"return_home_layout_5")
        self.return_home_layout_5.setContentsMargins(0, 0, 0, 0)
        self.label_89 = QLabel(self.recommended_apps_page_5)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(170, 270, 71, 51))
        self.label_89.setFont(font6)
        self.label_89.setStyleSheet(u"")
        self.label_89.setWordWrap(True)
        self.label_183 = QLabel(self.recommended_apps_page_5)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setGeometry(QRect(280, 530, 450, 91))
        self.label_183.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_184 = QLabel(self.recommended_apps_page_5)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(280, 350, 450, 71))
        self.label_184.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_185 = QLabel(self.recommended_apps_page_5)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(130, 60, 441, 51))
        self.label_185.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_186 = QLabel(self.recommended_apps_page_5)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(280, 260, 450, 71))
        self.label_186.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_187 = QLabel(self.recommended_apps_page_5)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(300, 190, 411, 31))
        self.label_187.setFont(font7)
        self.label_187.setStyleSheet(u"")
        self.label_187.setWordWrap(True)
        self.recc_app_install_frame_25 = QFrame(self.recommended_apps_page_5)
        self.recc_app_install_frame_25.setObjectName(u"recc_app_install_frame_25")
        self.recc_app_install_frame_25.setGeometry(QRect(770, 260, 131, 71))
        self.recc_app_install_frame_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_25.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_25.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_25.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_25.setLineWidth(0)
        self.recc_app_install_layout_1_22 = QHBoxLayout(self.recc_app_install_frame_25)
        self.recc_app_install_layout_1_22.setSpacing(0)
        self.recc_app_install_layout_1_22.setObjectName(u"recc_app_install_layout_1_22")
        self.recc_app_install_layout_1_22.setContentsMargins(0, 0, 0, 0)
        self.label_188 = QLabel(self.recommended_apps_page_5)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(160, 260, 91, 71))
        self.label_188.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_189 = QLabel(self.recommended_apps_page_5)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(160, 440, 91, 71))
        self.label_189.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_190 = QLabel(self.recommended_apps_page_5)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(600, 60, 361, 51))
        self.label_190.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_191 = QLabel(self.recommended_apps_page_5)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(160, 170, 91, 71))
        self.label_191.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_192 = QLabel(self.recommended_apps_page_5)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(170, 450, 71, 51))
        self.label_192.setFont(font6)
        self.label_192.setStyleSheet(u"")
        self.label_192.setWordWrap(True)
        self.label_193 = QLabel(self.recommended_apps_page_5)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(290, 460, 411, 31))
        self.label_193.setFont(font7)
        self.label_193.setStyleSheet(u"")
        self.label_193.setWordWrap(True)
        self.recc_next_page_frame_6 = QFrame(self.recommended_apps_page_5)
        self.recc_next_page_frame_6.setObjectName(u"recc_next_page_frame_6")
        self.recc_next_page_frame_6.setGeometry(QRect(1010, 360, 51, 261))
        self.recc_next_page_frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_next_page_frame_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_next_page_frame_6.setFrameShape(QFrame.NoFrame)
        self.recc_next_page_frame_6.setFrameShadow(QFrame.Raised)
        self.recc_next_page_frame_6.setLineWidth(0)
        self.recc_next_page_layout_5 = QHBoxLayout(self.recc_next_page_frame_6)
        self.recc_next_page_layout_5.setSpacing(0)
        self.recc_next_page_layout_5.setObjectName(u"recc_next_page_layout_5")
        self.recc_next_page_layout_5.setContentsMargins(0, 0, 0, 0)
        self.label_340 = QLabel(self.recommended_apps_page_5)
        self.label_340.setObjectName(u"label_340")
        self.label_340.setGeometry(QRect(1000, 350, 71, 281))
        self.label_340.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_22 = QLabel(self.recommended_apps_page_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(290, 560, 421, 61))
        self.label_22.setStyleSheet(u"color: teal")
        self.label_22.setWordWrap(True)
        self.stackedWidget.addWidget(self.recommended_apps_page_5)
        self.label_157.raise_()
        self.label_123.raise_()
        self.recc_app_install_frame_21.raise_()
        self.label_181.raise_()
        self.recc_app_install_frame_22.raise_()
        self.recc_app_install_frame_23.raise_()
        self.recc_app_install_frame_24.raise_()
        self.label_163.raise_()
        self.label_167.raise_()
        self.label_182.raise_()
        self.label_183.raise_()
        self.label_184.raise_()
        self.label_185.raise_()
        self.label_186.raise_()
        self.label_188.raise_()
        self.label_189.raise_()
        self.label_190.raise_()
        self.label_191.raise_()
        self.label_192.raise_()
        self.label_193.raise_()
        self.label_155.raise_()
        self.label_151.raise_()
        self.label_139.raise_()
        self.label_145.raise_()
        self.label_135.raise_()
        self.label_129.raise_()
        self.label_127.raise_()
        self.label_117.raise_()
        self.title_7.raise_()
        self.status_indicator_frame_5.raise_()
        self.recc_app_install_frame_25.raise_()
        self.label_95.raise_()
        self.label_89.raise_()
        self.label_187.raise_()
        self.back_button_frame_3.raise_()
        self.label_340.raise_()
        self.recc_next_page_frame_6.raise_()
        self.label_22.raise_()
        self.recommended_apps_page_6 = QWidget()
        self.recommended_apps_page_6.setObjectName(u"recommended_apps_page_6")
        self.status_indicator_frame_6 = QFrame(self.recommended_apps_page_6)
        self.status_indicator_frame_6.setObjectName(u"status_indicator_frame_6")
        self.status_indicator_frame_6.setGeometry(QRect(640, 70, 281, 51))
        self.status_indicator_frame_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_indicator_frame_6.setStyleSheet(u"")
        self.status_indicator_frame_6.setFrameShape(QFrame.NoFrame)
        self.status_indicator_frame_6.setFrameShadow(QFrame.Raised)
        self.status_indicator_frame_6.setLineWidth(0)
        self.status_indicator_layout_6 = QHBoxLayout(self.status_indicator_frame_6)
        self.status_indicator_layout_6.setSpacing(0)
        self.status_indicator_layout_6.setObjectName(u"status_indicator_layout_6")
        self.status_indicator_layout_6.setContentsMargins(0, 0, 0, 0)
        self.label_194 = QLabel(self.recommended_apps_page_6)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(160, 260, 91, 71))
        self.label_194.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_195 = QLabel(self.recommended_apps_page_6)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(300, 190, 411, 31))
        self.label_195.setFont(font7)
        self.label_195.setStyleSheet(u"")
        self.label_195.setWordWrap(True)
        self.label_196 = QLabel(self.recommended_apps_page_6)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(170, 190, 71, 31))
        self.label_196.setFont(font6)
        self.label_196.setStyleSheet(u"")
        self.label_197 = QLabel(self.recommended_apps_page_6)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(280, 440, 450, 71))
        self.label_197.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_198 = QLabel(self.recommended_apps_page_6)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(280, 170, 450, 71))
        self.label_198.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.recc_app_install_frame_26 = QFrame(self.recommended_apps_page_6)
        self.recc_app_install_frame_26.setObjectName(u"recc_app_install_frame_26")
        self.recc_app_install_frame_26.setGeometry(QRect(770, 170, 131, 71))
        self.recc_app_install_frame_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_26.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_26.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_26.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_26.setLineWidth(0)
        self.recc_app_install_layout_1_26 = QHBoxLayout(self.recc_app_install_frame_26)
        self.recc_app_install_layout_1_26.setSpacing(0)
        self.recc_app_install_layout_1_26.setObjectName(u"recc_app_install_layout_1_26")
        self.recc_app_install_layout_1_26.setContentsMargins(0, 0, 0, 0)
        self.title_11 = QLabel(self.recommended_apps_page_6)
        self.title_11.setObjectName(u"title_11")
        self.title_11.setGeometry(QRect(160, 75, 331, 41))
        self.title_11.setFont(font8)
        self.title_11.setStyleSheet(u"")
        self.title_11.setAlignment(Qt.AlignCenter)
        self.label_199 = QLabel(self.recommended_apps_page_6)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(160, 440, 91, 71))
        self.label_199.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.back_button_frame_9 = QFrame(self.recommended_apps_page_6)
        self.back_button_frame_9.setObjectName(u"back_button_frame_9")
        self.back_button_frame_9.setGeometry(QRect(1010, 150, 51, 181))
        self.back_button_frame_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_9.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_9.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_9.setFrameShadow(QFrame.Raised)
        self.back_button_frame_9.setLineWidth(0)
        self.return_home_layout_6 = QHBoxLayout(self.back_button_frame_9)
        self.return_home_layout_6.setSpacing(0)
        self.return_home_layout_6.setObjectName(u"return_home_layout_6")
        self.return_home_layout_6.setContentsMargins(0, 0, 0, 0)
        self.label_200 = QLabel(self.recommended_apps_page_6)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(30, 50, 1071, 611))
        self.label_200.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_201 = QLabel(self.recommended_apps_page_6)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(280, 350, 450, 71))
        self.label_201.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_202 = QLabel(self.recommended_apps_page_6)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(290, 550, 411, 31))
        self.label_202.setFont(font7)
        self.label_202.setStyleSheet(u"")
        self.label_202.setWordWrap(True)
        self.recc_next_page_frame_7 = QFrame(self.recommended_apps_page_6)
        self.recc_next_page_frame_7.setObjectName(u"recc_next_page_frame_7")
        self.recc_next_page_frame_7.setGeometry(QRect(1010, 360, 51, 261))
        self.recc_next_page_frame_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_next_page_frame_7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_next_page_frame_7.setFrameShape(QFrame.NoFrame)
        self.recc_next_page_frame_7.setFrameShadow(QFrame.Raised)
        self.recc_next_page_frame_7.setLineWidth(0)
        self.recc_next_page_layout_6 = QHBoxLayout(self.recc_next_page_frame_7)
        self.recc_next_page_layout_6.setSpacing(0)
        self.recc_next_page_layout_6.setObjectName(u"recc_next_page_layout_6")
        self.recc_next_page_layout_6.setContentsMargins(0, 0, 0, 0)
        self.label_203 = QLabel(self.recommended_apps_page_6)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(160, 170, 91, 71))
        self.label_203.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_204 = QLabel(self.recommended_apps_page_6)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(300, 370, 411, 31))
        self.label_204.setFont(font7)
        self.label_204.setStyleSheet(u"")
        self.label_204.setWordWrap(True)
        self.label_205 = QLabel(self.recommended_apps_page_6)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(160, 530, 91, 71))
        self.label_205.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_206 = QLabel(self.recommended_apps_page_6)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(160, 350, 91, 71))
        self.label_206.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_207 = QLabel(self.recommended_apps_page_6)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(290, 460, 411, 31))
        self.label_207.setFont(font7)
        self.label_207.setStyleSheet(u"")
        self.label_207.setWordWrap(True)
        self.recc_app_install_frame_27 = QFrame(self.recommended_apps_page_6)
        self.recc_app_install_frame_27.setObjectName(u"recc_app_install_frame_27")
        self.recc_app_install_frame_27.setGeometry(QRect(770, 260, 131, 71))
        self.recc_app_install_frame_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_27.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_27.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_27.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_27.setLineWidth(0)
        self.recc_app_install_layout_1_27 = QHBoxLayout(self.recc_app_install_frame_27)
        self.recc_app_install_layout_1_27.setSpacing(0)
        self.recc_app_install_layout_1_27.setObjectName(u"recc_app_install_layout_1_27")
        self.recc_app_install_layout_1_27.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_28 = QFrame(self.recommended_apps_page_6)
        self.recc_app_install_frame_28.setObjectName(u"recc_app_install_frame_28")
        self.recc_app_install_frame_28.setGeometry(QRect(770, 530, 131, 71))
        self.recc_app_install_frame_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_28.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_28.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_28.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_28.setLineWidth(0)
        self.recc_app_install_layout_25 = QHBoxLayout(self.recc_app_install_frame_28)
        self.recc_app_install_layout_25.setSpacing(0)
        self.recc_app_install_layout_25.setObjectName(u"recc_app_install_layout_25")
        self.recc_app_install_layout_25.setContentsMargins(0, 0, 0, 0)
        self.label_341 = QLabel(self.recommended_apps_page_6)
        self.label_341.setObjectName(u"label_341")
        self.label_341.setGeometry(QRect(980, 130, 111, 511))
        self.label_341.setStyleSheet(u"QLabel {\n"
"        	\n"
"			\n"
"	background-color: rgb(212, 212, 212);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_208 = QLabel(self.recommended_apps_page_6)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(80, 130, 891, 511))
        self.label_208.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_209 = QLabel(self.recommended_apps_page_6)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(170, 450, 71, 51))
        self.label_209.setFont(font6)
        self.label_209.setStyleSheet(u"")
        self.label_209.setWordWrap(True)
        self.label_342 = QLabel(self.recommended_apps_page_6)
        self.label_342.setObjectName(u"label_342")
        self.label_342.setGeometry(QRect(1000, 350, 71, 281))
        self.label_342.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_210 = QLabel(self.recommended_apps_page_6)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setGeometry(QRect(590, 80, 51, 31))
        self.label_210.setFont(font6)
        self.label_210.setStyleSheet(u"")
        self.label_211 = QLabel(self.recommended_apps_page_6)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setGeometry(QRect(280, 530, 450, 71))
        self.label_211.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_212 = QLabel(self.recommended_apps_page_6)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setGeometry(QRect(170, 540, 71, 51))
        self.label_212.setFont(font6)
        self.label_212.setStyleSheet(u"")
        self.label_212.setWordWrap(True)
        self.label_213 = QLabel(self.recommended_apps_page_6)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setGeometry(QRect(280, 260, 450, 71))
        self.label_213.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_214 = QLabel(self.recommended_apps_page_6)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(170, 370, 71, 31))
        self.label_214.setFont(font6)
        self.label_214.setStyleSheet(u"")
        self.recc_app_install_frame_29 = QFrame(self.recommended_apps_page_6)
        self.recc_app_install_frame_29.setObjectName(u"recc_app_install_frame_29")
        self.recc_app_install_frame_29.setGeometry(QRect(770, 440, 131, 71))
        self.recc_app_install_frame_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_29.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_29.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_29.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_29.setLineWidth(0)
        self.recc_app_install_layout_26 = QHBoxLayout(self.recc_app_install_frame_29)
        self.recc_app_install_layout_26.setSpacing(0)
        self.recc_app_install_layout_26.setObjectName(u"recc_app_install_layout_26")
        self.recc_app_install_layout_26.setContentsMargins(0, 0, 0, 0)
        self.label_215 = QLabel(self.recommended_apps_page_6)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(110, 70, 441, 51))
        self.label_215.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_216 = QLabel(self.recommended_apps_page_6)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(580, 70, 361, 51))
        self.label_216.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_217 = QLabel(self.recommended_apps_page_6)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(300, 280, 411, 31))
        self.label_217.setFont(font7)
        self.label_217.setStyleSheet(u"")
        self.label_217.setWordWrap(True)
        self.label_218 = QLabel(self.recommended_apps_page_6)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(170, 280, 71, 31))
        self.label_218.setFont(font6)
        self.label_218.setStyleSheet(u"")
        self.recc_app_install_frame_30 = QFrame(self.recommended_apps_page_6)
        self.recc_app_install_frame_30.setObjectName(u"recc_app_install_frame_30")
        self.recc_app_install_frame_30.setGeometry(QRect(770, 350, 131, 71))
        self.recc_app_install_frame_30.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_30.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_30.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_30.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_30.setLineWidth(0)
        self.recc_app_install_layout_27 = QHBoxLayout(self.recc_app_install_frame_30)
        self.recc_app_install_layout_27.setSpacing(0)
        self.recc_app_install_layout_27.setObjectName(u"recc_app_install_layout_27")
        self.recc_app_install_layout_27.setContentsMargins(0, 0, 0, 0)
        self.label_343 = QLabel(self.recommended_apps_page_6)
        self.label_343.setObjectName(u"label_343")
        self.label_343.setGeometry(QRect(1000, 140, 71, 201))
        self.label_343.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.stackedWidget.addWidget(self.recommended_apps_page_6)
        self.label_200.raise_()
        self.label_208.raise_()
        self.label_197.raise_()
        self.label_198.raise_()
        self.recc_app_install_frame_26.raise_()
        self.label_199.raise_()
        self.label_201.raise_()
        self.label_203.raise_()
        self.label_204.raise_()
        self.label_205.raise_()
        self.label_206.raise_()
        self.label_207.raise_()
        self.recc_app_install_frame_27.raise_()
        self.recc_app_install_frame_28.raise_()
        self.label_341.raise_()
        self.label_209.raise_()
        self.label_342.raise_()
        self.label_211.raise_()
        self.label_212.raise_()
        self.label_213.raise_()
        self.label_214.raise_()
        self.recc_app_install_frame_29.raise_()
        self.label_215.raise_()
        self.label_216.raise_()
        self.label_217.raise_()
        self.recc_app_install_frame_30.raise_()
        self.label_343.raise_()
        self.label_194.raise_()
        self.label_202.raise_()
        self.label_195.raise_()
        self.label_196.raise_()
        self.label_210.raise_()
        self.label_218.raise_()
        self.title_11.raise_()
        self.back_button_frame_9.raise_()
        self.recc_next_page_frame_7.raise_()
        self.status_indicator_frame_6.raise_()
        self.recommended_apps_page_1 = QWidget()
        self.recommended_apps_page_1.setObjectName(u"recommended_apps_page_1")
        self.label_86 = QLabel(self.recommended_apps_page_1)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(280, 260, 450, 71))
        self.label_86.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_87 = QLabel(self.recommended_apps_page_1)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(280, 350, 450, 71))
        self.label_87.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_88 = QLabel(self.recommended_apps_page_1)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(170, 270, 71, 51))
        self.label_88.setFont(font6)
        self.label_88.setStyleSheet(u"")
        self.label_88.setWordWrap(True)
        self.label_90 = QLabel(self.recommended_apps_page_1)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(300, 370, 411, 31))
        self.label_90.setFont(font7)
        self.label_90.setStyleSheet(u"")
        self.label_90.setWordWrap(True)
        self.label_91 = QLabel(self.recommended_apps_page_1)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(160, 530, 91, 71))
        self.label_91.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_92 = QLabel(self.recommended_apps_page_1)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(170, 190, 71, 31))
        self.label_92.setFont(font6)
        self.label_92.setStyleSheet(u"")
        self.label_93 = QLabel(self.recommended_apps_page_1)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(290, 550, 411, 31))
        self.label_93.setFont(font7)
        self.label_93.setStyleSheet(u"")
        self.label_93.setWordWrap(True)
        self.label_94 = QLabel(self.recommended_apps_page_1)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(280, 530, 450, 71))
        self.label_94.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_96 = QLabel(self.recommended_apps_page_1)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(30, 50, 1071, 611))
        self.label_96.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_97 = QLabel(self.recommended_apps_page_1)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(290, 460, 411, 31))
        self.label_97.setFont(font7)
        self.label_97.setStyleSheet(u"")
        self.label_97.setWordWrap(True)
        self.label_98 = QLabel(self.recommended_apps_page_1)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(80, 130, 891, 511))
        self.label_98.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_100 = QLabel(self.recommended_apps_page_1)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(300, 190, 411, 31))
        self.label_100.setFont(font7)
        self.label_100.setStyleSheet(u"")
        self.label_100.setWordWrap(True)
        self.label_101 = QLabel(self.recommended_apps_page_1)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(130, 60, 441, 51))
        self.label_101.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_102 = QLabel(self.recommended_apps_page_1)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(160, 170, 91, 71))
        self.label_102.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_103 = QLabel(self.recommended_apps_page_1)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(170, 370, 71, 31))
        self.label_103.setFont(font6)
        self.label_103.setStyleSheet(u"")
        self.label_104 = QLabel(self.recommended_apps_page_1)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(170, 450, 71, 51))
        self.label_104.setFont(font6)
        self.label_104.setStyleSheet(u"")
        self.label_104.setWordWrap(True)
        self.label_105 = QLabel(self.recommended_apps_page_1)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(280, 440, 450, 71))
        self.label_105.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_106 = QLabel(self.recommended_apps_page_1)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(280, 170, 450, 71))
        self.label_106.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_108 = QLabel(self.recommended_apps_page_1)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(170, 540, 71, 51))
        self.label_108.setFont(font6)
        self.label_108.setStyleSheet(u"")
        self.label_108.setWordWrap(True)
        self.label_109 = QLabel(self.recommended_apps_page_1)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(160, 350, 91, 71))
        self.label_109.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_110 = QLabel(self.recommended_apps_page_1)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(160, 440, 91, 71))
        self.label_110.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.title_5 = QLabel(self.recommended_apps_page_1)
        self.title_5.setObjectName(u"title_5")
        self.title_5.setGeometry(QRect(180, 65, 331, 41))
        self.title_5.setFont(font8)
        self.title_5.setStyleSheet(u"")
        self.title_5.setAlignment(Qt.AlignCenter)
        self.label_112 = QLabel(self.recommended_apps_page_1)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(160, 260, 91, 71))
        self.label_112.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_113 = QLabel(self.recommended_apps_page_1)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(300, 280, 411, 31))
        self.label_113.setFont(font7)
        self.label_113.setStyleSheet(u"")
        self.label_113.setWordWrap(True)
        self.recc_app_install_frame_2 = QFrame(self.recommended_apps_page_1)
        self.recc_app_install_frame_2.setObjectName(u"recc_app_install_frame_2")
        self.recc_app_install_frame_2.setGeometry(QRect(770, 260, 131, 71))
        self.recc_app_install_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_2.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_2.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_2.setLineWidth(0)
        self.recc_app_install_layout_2 = QHBoxLayout(self.recc_app_install_frame_2)
        self.recc_app_install_layout_2.setSpacing(0)
        self.recc_app_install_layout_2.setObjectName(u"recc_app_install_layout_2")
        self.recc_app_install_layout_2.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_3 = QFrame(self.recommended_apps_page_1)
        self.recc_app_install_frame_3.setObjectName(u"recc_app_install_frame_3")
        self.recc_app_install_frame_3.setGeometry(QRect(770, 350, 131, 71))
        self.recc_app_install_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_3.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_3.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_3.setLineWidth(0)
        self.recc_app_install_layout_3 = QHBoxLayout(self.recc_app_install_frame_3)
        self.recc_app_install_layout_3.setSpacing(0)
        self.recc_app_install_layout_3.setObjectName(u"recc_app_install_layout_3")
        self.recc_app_install_layout_3.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_4 = QFrame(self.recommended_apps_page_1)
        self.recc_app_install_frame_4.setObjectName(u"recc_app_install_frame_4")
        self.recc_app_install_frame_4.setGeometry(QRect(770, 440, 131, 71))
        self.recc_app_install_frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_4.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_4.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_4.setLineWidth(0)
        self.recc_app_install_layout_4 = QHBoxLayout(self.recc_app_install_frame_4)
        self.recc_app_install_layout_4.setSpacing(0)
        self.recc_app_install_layout_4.setObjectName(u"recc_app_install_layout_4")
        self.recc_app_install_layout_4.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_5 = QFrame(self.recommended_apps_page_1)
        self.recc_app_install_frame_5.setObjectName(u"recc_app_install_frame_5")
        self.recc_app_install_frame_5.setGeometry(QRect(770, 530, 131, 71))
        self.recc_app_install_frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_5.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_5.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_5.setLineWidth(0)
        self.recc_app_install_layout_5 = QHBoxLayout(self.recc_app_install_frame_5)
        self.recc_app_install_layout_5.setSpacing(0)
        self.recc_app_install_layout_5.setObjectName(u"recc_app_install_layout_5")
        self.recc_app_install_layout_5.setContentsMargins(0, 0, 0, 0)
        self.label_170 = QLabel(self.recommended_apps_page_1)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(600, 60, 361, 51))
        self.label_170.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	      background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 12px;\n"
"			border-bottom: 30px shadow;\n"
"        }\n"
"")
        self.label_171 = QLabel(self.recommended_apps_page_1)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(610, 70, 51, 31))
        self.label_171.setFont(font6)
        self.label_171.setStyleSheet(u"")
        self.status_indicator_frame_1 = QFrame(self.recommended_apps_page_1)
        self.status_indicator_frame_1.setObjectName(u"status_indicator_frame_1")
        self.status_indicator_frame_1.setGeometry(QRect(660, 60, 281, 51))
        self.status_indicator_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.status_indicator_frame_1.setStyleSheet(u"")
        self.status_indicator_frame_1.setFrameShape(QFrame.NoFrame)
        self.status_indicator_frame_1.setFrameShadow(QFrame.Raised)
        self.status_indicator_frame_1.setLineWidth(0)
        self.status_indicator_layout_1 = QHBoxLayout(self.status_indicator_frame_1)
        self.status_indicator_layout_1.setSpacing(0)
        self.status_indicator_layout_1.setObjectName(u"status_indicator_layout_1")
        self.status_indicator_layout_1.setContentsMargins(0, 0, 0, 0)
        self.recc_app_install_frame_1 = QFrame(self.recommended_apps_page_1)
        self.recc_app_install_frame_1.setObjectName(u"recc_app_install_frame_1")
        self.recc_app_install_frame_1.setGeometry(QRect(770, 170, 131, 71))
        self.recc_app_install_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_app_install_frame_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(194, 234, 189);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_app_install_frame_1.setFrameShape(QFrame.NoFrame)
        self.recc_app_install_frame_1.setFrameShadow(QFrame.Raised)
        self.recc_app_install_frame_1.setLineWidth(0)
        self.recc_app_install_layout_1 = QHBoxLayout(self.recc_app_install_frame_1)
        self.recc_app_install_layout_1.setSpacing(0)
        self.recc_app_install_layout_1.setObjectName(u"recc_app_install_layout_1")
        self.recc_app_install_layout_1.setContentsMargins(0, 0, 0, 0)
        self.back_button_frame_2 = QFrame(self.recommended_apps_page_1)
        self.back_button_frame_2.setObjectName(u"back_button_frame_2")
        self.back_button_frame_2.setGeometry(QRect(1010, 150, 51, 181))
        self.back_button_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button_frame_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.back_button_frame_2.setFrameShape(QFrame.NoFrame)
        self.back_button_frame_2.setFrameShadow(QFrame.Raised)
        self.back_button_frame_2.setLineWidth(0)
        self.return_home_layout_1 = QHBoxLayout(self.back_button_frame_2)
        self.return_home_layout_1.setSpacing(0)
        self.return_home_layout_1.setObjectName(u"return_home_layout_1")
        self.return_home_layout_1.setContentsMargins(0, 0, 0, 0)
        self.recc_next_page_frame_1 = QFrame(self.recommended_apps_page_1)
        self.recc_next_page_frame_1.setObjectName(u"recc_next_page_frame_1")
        self.recc_next_page_frame_1.setGeometry(QRect(1010, 360, 51, 261))
        self.recc_next_page_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.recc_next_page_frame_1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 16pt \"Montserrat\";\n"
"	background-color: rgb(197, 238, 203);\n"
"	padding: 12px;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(238, 255, 231);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 197, 163);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"}")
        self.recc_next_page_frame_1.setFrameShape(QFrame.NoFrame)
        self.recc_next_page_frame_1.setFrameShadow(QFrame.Raised)
        self.recc_next_page_frame_1.setLineWidth(0)
        self.recc_next_page_layout_1 = QHBoxLayout(self.recc_next_page_frame_1)
        self.recc_next_page_layout_1.setSpacing(0)
        self.recc_next_page_layout_1.setObjectName(u"recc_next_page_layout_1")
        self.recc_next_page_layout_1.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.recommended_apps_page_1)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(1000, 140, 71, 201))
        self.label_99.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_107 = QLabel(self.recommended_apps_page_1)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(1000, 350, 71, 281))
        self.label_107.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(197, 197, 197);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_111 = QLabel(self.recommended_apps_page_1)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(980, 130, 111, 511))
        self.label_111.setStyleSheet(u"QLabel {\n"
"        	\n"
"			\n"
"	background-color: rgb(212, 212, 212);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.stackedWidget.addWidget(self.recommended_apps_page_1)
        self.label_96.raise_()
        self.label_111.raise_()
        self.label_98.raise_()
        self.label_101.raise_()
        self.label_102.raise_()
        self.label_105.raise_()
        self.label_106.raise_()
        self.label_109.raise_()
        self.label_110.raise_()
        self.title_5.raise_()
        self.label_112.raise_()
        self.label_100.raise_()
        self.label_87.raise_()
        self.label_88.raise_()
        self.label_90.raise_()
        self.label_92.raise_()
        self.label_91.raise_()
        self.label_94.raise_()
        self.label_93.raise_()
        self.label_97.raise_()
        self.label_108.raise_()
        self.label_104.raise_()
        self.label_103.raise_()
        self.label_86.raise_()
        self.label_113.raise_()
        self.recc_app_install_frame_2.raise_()
        self.recc_app_install_frame_3.raise_()
        self.recc_app_install_frame_4.raise_()
        self.recc_app_install_frame_5.raise_()
        self.label_170.raise_()
        self.label_171.raise_()
        self.status_indicator_frame_1.raise_()
        self.recc_app_install_frame_1.raise_()
        self.label_99.raise_()
        self.label_107.raise_()
        self.back_button_frame_2.raise_()
        self.recc_next_page_frame_1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Search and install apps", None))
        self.title_3.setText(QCoreApplication.translate("MainWindow", u"Home Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Manage settings", None))
        self.label_21.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Recommended Apps", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Add/remove/update scoop buckets/apps", None))
        self.label_57.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Faster Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Use Download Manager", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Some other setting", None))
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_60.setText("")
        self.label_63.setText("")
        self.title_4.setText(QCoreApplication.translate("MainWindow", u"Loading Scoop Gui..", None))
        self.label_66.setText("")
        self.label_69.setText("")
        self.title_6.setText(QCoreApplication.translate("MainWindow", u"An app by Faraz Ahary and Thomas Kerby", None))
        self.label_72.setText("")
        self.title_buckets.setText(QCoreApplication.translate("MainWindow", u"Manage Buckets", None))
        self.add_bucket_title.setText(QCoreApplication.translate("MainWindow", u"Add Bucket", None))
        self.bucket_input_add.setText(QCoreApplication.translate("MainWindow", u"Bucket Name / URL", None))
#if QT_CONFIG(tooltip)
        self.bucket_button_add.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>test</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bucket_button_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_bucket_title.setText(QCoreApplication.translate("MainWindow", u"Remove Bucket", None))
        self.bucket_button_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.title_buckets_2.setText(QCoreApplication.translate("MainWindow", u"Manage Buckets", None))
        self.label_46.setText("")
        self.label_47.setText("")
        self.label_48.setText("")
        self.title_buckets_3.setText(QCoreApplication.translate("MainWindow", u"Manage Apps", None))
        self.label_49.setText("")
        self.label_50.setText("")
        self.label_51.setText("")
        self.label_52.setText("")
        self.label_53.setText("")
        self.label_54.setText("")
        self.label_55.setText("")
        self.title_buckets_4.setText(QCoreApplication.translate("MainWindow", u"Update all", None))
        self.title_buckets_5.setText(QCoreApplication.translate("MainWindow", u"remove app", None))
        self.title_buckets_6.setText(QCoreApplication.translate("MainWindow", u"Cleanup old app versions", None))
        self.label_27.setText("")
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.label_33.setText("")
        self.label_34.setText("")
        self.label_35.setText("")
        self.label_36.setText("")
        self.label_37.setText("")
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.label_41.setText("")
        self.label_42.setText("")
        self.label_43.setText("")
        self.label_44.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Apps", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_58.setText("")
        self.label_59.setText("")
        self.label_61.setText("")
        self.label_62.setText("")
        self.label_64.setText("")
        self.label_65.setText("")
        self.label_67.setText("")
        self.label_68.setText("")
        self.label_70.setText("")
        self.label_71.setText("")
        self.label_73.setText("")
        self.label_74.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Peazip", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Fast compression utility, also supports ARC which is the best algo for day to day usage - (foss)", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Librewolf", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Fork of firefox - browser made with privacy and security in mind - (foss)", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Freetube", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Desktop youtube client - no ads, skips sponsors - (foss)", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Geek uninstaller", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Fork of bcuninstaller but with a modern gui - actually good app uninstaller", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Simplewall", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Block internet access for apps, increases privacy/security, also prevents malware for example collecting data - (foss)", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.title_8.setText(QCoreApplication.translate("MainWindow", u"Recommended Apps - Page 2/6", None))
        self.label_173.setText("")
        self.label_174.setText("")
        self.label_331.setText("")
        self.label_332.setText("")
        self.label_333.setText("")
        self.label_114.setText("")
        self.label_115.setText("")
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Playnite", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Check hdd/sdd life - (foss)", None))
        self.label_119.setText("")
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Sandboxie Plus", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Stress test ram, gpu, cpu to check their max temperatures, or to check stability", None))
        self.label_122.setText("")
        self.label_124.setText("")
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Check hardware temperatures", None))
        self.label_126.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Because windows literally has no sandboxing on non-microsoft-store apps which is what makes malware so common, sandbox untrustworthy apps. - (foss)", None))
        self.label_130.setText("")
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Crystal Disk Info", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Hwinfo", None))
        self.label_133.setText("")
        self.label_134.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"OCCT", None))
        self.label_137.setText("")
        self.label_138.setText("")
        self.label_140.setText("")
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Modern, extensible, game launcher - (foss)", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.title_9.setText(QCoreApplication.translate("MainWindow", u"Recommended Apps - Page 3/6", None))
        self.label_176.setText("")
        self.label_177.setText("")
        self.label_334.setText("")
        self.label_335.setText("")
        self.label_336.setText("")
        self.label_142.setText("")
        self.label_143.setText("")
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"MPV", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Modern ssh client - (foss)", None))
        self.label_147.setText("")
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"ShutUp10", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Very stable nintendo switch emulator, less graphical bugs than yuzu, also allows importing shader cache (gets rid of first time stutters entirely) - (foss)", None))
        self.label_150.setText("")
        self.label_152.setText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Control audio volume per apps, replaces windows audio button on taskbar, same design - (foss)", None))
        self.label_154.setText("")
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Tries to lessen the amount of telemetry collected by windows", None))
        self.label_158.setText("")
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Tabby", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Ear Trumpet", None))
        self.label_161.setText("")
        self.label_162.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Ryujinx", None))
        self.label_165.setText("")
        self.label_166.setText("")
        self.label_168.setText("")
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"Fast, minimal media player - (foss)", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_179.setText("")
        self.title_10.setText(QCoreApplication.translate("MainWindow", u"Recommended Apps - Page 4/6", None))
        self.label_180.setText("")
        self.label_337.setText("")
        self.label_338.setText("")
        self.label_339.setText("")
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Useful text expander for keyboard warriors - for e.g typing :q in a messaging application which pastes a custom piece of text - (foss)", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Foss alternative to wallpaper engine - animated desktop background - (foss)", None))
        self.label_123.setText("")
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Lively", None))
        self.label_129.setText("")
        self.label_135.setText("")
        self.label_139.setText("")
        self.label_145.setText("")
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Foss and non-intrusive tool to update drivers, most useful if encountering issues/BSOD's, or for updating gpu drivers for better performance. ", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Modern Flyouts", None))
        self.label_157.setText("")
        self.title_7.setText(QCoreApplication.translate("MainWindow", u"Recommended Apps - Page 5/6", None))
        self.label_163.setText("")
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"SDIO", None))
        self.label_182.setText("")
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Espanso", None))
        self.label_183.setText("")
        self.label_184.setText("")
        self.label_185.setText("")
        self.label_186.setText("")
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Modern replacment for the ancient windows media flyout/widget - (foss)", None))
        self.label_188.setText("")
        self.label_189.setText("")
        self.label_190.setText("")
        self.label_191.setText("")
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Obsidian", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"Modern and very powerful knowledge organiser/note client - uses LaTeX or md", None))
        self.label_340.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"NOTE: that SDIO uses the torrent protocol to download drivers, whilst this is perfectly legal since the actual material downloaded is legal, it may still trigger red flags for some pedantic isp's", None))
        self.label_194.setText("")
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Modern and foss utility to modify fan curves", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"FanControl", None))
        self.label_197.setText("")
        self.label_198.setText("")
        self.title_11.setText(QCoreApplication.translate("MainWindow", u"Recommended Apps - Page 6/6", None))
        self.label_199.setText("")
        self.label_200.setText("")
        self.label_201.setText("")
        self.label_202.setText("")
        self.label_203.setText("")
        self.label_204.setText("")
        self.label_205.setText("")
        self.label_206.setText("")
        self.label_207.setText("")
        self.label_341.setText("")
        self.label_208.setText("")
        self.label_209.setText("")
        self.label_342.setText("")
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_211.setText("")
        self.label_212.setText("")
        self.label_213.setText("")
        self.label_214.setText("")
        self.label_215.setText("")
        self.label_216.setText("")
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Change rgb without installing annoying manufacterer apps - foss", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"OpenRGB", None))
        self.label_343.setText("")
        self.label_86.setText("")
        self.label_87.setText("")
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Fluent Reader", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Beautiful screenshot utility - (foss)", None))
        self.label_91.setText("")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Portmaster", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Compress games without any impact on speed, saves huge amounts of storage on many games - (foss)", None))
        self.label_94.setText("")
        self.label_96.setText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Backup game saves easily - (foss)", None))
        self.label_98.setText("")
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Decent alternative to pihole/adguard home if you can't selfhost them, also replaces simplewall. - (foss)", None))
        self.label_101.setText("")
        self.label_102.setText("")
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Flameshot", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Ludusavi", None))
        self.label_105.setText("")
        self.label_106.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Compact GUI", None))
        self.label_109.setText("")
        self.label_110.setText("")
        self.title_5.setText(QCoreApplication.translate("MainWindow", u"Recommended Apps - Page 1/6", None))
        self.label_112.setText("")
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Modern RSS (news) client - (foss)", None))
        self.label_170.setText("")
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_99.setText("")
        self.label_107.setText("")
        self.label_111.setText("")
    # retranslateUi


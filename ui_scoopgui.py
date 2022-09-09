# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoopguieDHOkV.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1083, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, -21, 1071, 601))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.search_layout = QFrame(self.home)
        self.search_layout.setObjectName(u"search_layout")
        self.search_layout.setGeometry(QRect(480, 230, 220, 71))
        self.search_layout.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_layout.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.search_layout.setFrameShape(QFrame.NoFrame)
        self.search_layout.setFrameShadow(QFrame.Raised)
        self.search_layout.setLineWidth(0)
        self.enter_search_layout = QHBoxLayout(self.search_layout)
        self.enter_search_layout.setSpacing(0)
        self.enter_search_layout.setObjectName(u"enter_search_layout")
        self.enter_search_layout.setContentsMargins(0, 0, 0, 0)
        self.manage_appsbuckets_frame = QFrame(self.home)
        self.manage_appsbuckets_frame.setObjectName(u"manage_appsbuckets_frame")
        self.manage_appsbuckets_frame.setGeometry(QRect(480, 330, 220, 71))
        self.manage_appsbuckets_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.manage_appsbuckets_frame.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.manage_appsbuckets_frame.setFrameShape(QFrame.NoFrame)
        self.manage_appsbuckets_frame.setFrameShadow(QFrame.Raised)
        self.manage_appsbuckets_frame.setLineWidth(0)
        self.enter_manage_buckets_layout = QHBoxLayout(self.manage_appsbuckets_frame)
        self.enter_manage_buckets_layout.setSpacing(0)
        self.enter_manage_buckets_layout.setObjectName(u"enter_manage_buckets_layout")
        self.enter_manage_buckets_layout.setContentsMargins(0, 0, 0, 0)
        self.settings_frame = QFrame(self.home)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setGeometry(QRect(490, 430, 220, 71))
        self.settings_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_frame.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.settings_frame.setFrameShape(QFrame.NoFrame)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.settings_frame.setLineWidth(0)
        self.settings_page_layout = QHBoxLayout(self.settings_frame)
        self.settings_page_layout.setSpacing(0)
        self.settings_page_layout.setObjectName(u"settings_page_layout")
        self.settings_page_layout.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.home)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(290, 110, 441, 91))
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
        self.label_20.setGeometry(QRect(290, 320, 171, 91))
        self.label_20.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_4 = QLabel(self.home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 250, 141, 31))
        self.label_4.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_4.setWordWrap(True)
        self.title_3 = QLabel(self.home)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(330, 140, 351, 41))
        font = QFont()
        font.setPointSize(16)
        self.title_3.setFont(font)
        self.title_3.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.title_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 450, 131, 31))
        self.label_5.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_21 = QLabel(self.home)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(290, 420, 171, 91))
        self.label_21.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_22 = QLabel(self.home)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(470, 420, 251, 91))
        self.label_22.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_23 = QLabel(self.home)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(290, 220, 171, 91))
        self.label_23.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_24 = QLabel(self.home)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(250, 90, 521, 471))
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
        self.label_6.setGeometry(QRect(310, 350, 141, 31))
        self.label_6.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_6.setWordWrap(True)
        self.label_25 = QLabel(self.home)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(470, 320, 251, 91))
        self.label_25.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_26 = QLabel(self.home)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(470, 220, 251, 91))
        self.label_26.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.stackedWidget.addWidget(self.home)
        self.label_24.raise_()
        self.label_26.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_25.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.title_3.raise_()
        self.search_layout.raise_()
        self.manage_appsbuckets_frame.raise_()
        self.settings_frame.raise_()
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.manage_buckets_frame_2 = QFrame(self.settings_page)
        self.manage_buckets_frame_2.setObjectName(u"manage_buckets_frame_2")
        self.manage_buckets_frame_2.setGeometry(QRect(530, 220, 131, 71))
        self.manage_buckets_frame_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.manage_buckets_frame_2.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_2.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_2.setLineWidth(0)
        self.settings_toggle_1_layout = QHBoxLayout(self.manage_buckets_frame_2)
        self.settings_toggle_1_layout.setSpacing(0)
        self.settings_toggle_1_layout.setObjectName(u"settings_toggle_1_layout")
        self.settings_toggle_1_layout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.settings_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(290, 210, 171, 91))
        self.label_11.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_12 = QLabel(self.settings_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(290, 310, 171, 91))
        self.label_12.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_13 = QLabel(self.settings_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(290, 410, 171, 91))
        self.label_13.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.manage_buckets_frame_3 = QFrame(self.settings_page)
        self.manage_buckets_frame_3.setObjectName(u"manage_buckets_frame_3")
        self.manage_buckets_frame_3.setGeometry(QRect(530, 320, 131, 71))
        self.manage_buckets_frame_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.manage_buckets_frame_3.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_3.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_3.setLineWidth(0)
        self.settings_toggle_2_layout = QHBoxLayout(self.manage_buckets_frame_3)
        self.settings_toggle_2_layout.setSpacing(0)
        self.settings_toggle_2_layout.setObjectName(u"settings_toggle_2_layout")
        self.settings_toggle_2_layout.setContentsMargins(0, 0, 0, 0)
        self.manage_buckets_frame_4 = QFrame(self.settings_page)
        self.manage_buckets_frame_4.setObjectName(u"manage_buckets_frame_4")
        self.manage_buckets_frame_4.setGeometry(QRect(530, 420, 131, 71))
        self.manage_buckets_frame_4.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.manage_buckets_frame_4.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_4.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_4.setLineWidth(0)
        self.settings_toggle_3_layout = QHBoxLayout(self.manage_buckets_frame_4)
        self.settings_toggle_3_layout.setSpacing(0)
        self.settings_toggle_3_layout.setObjectName(u"settings_toggle_3_layout")
        self.settings_toggle_3_layout.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.settings_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(290, 100, 441, 91))
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
        self.title_2.setGeometry(QRect(330, 130, 351, 41))
        self.title_2.setFont(font)
        self.title_2.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.title_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.settings_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 240, 81, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_2 = QLabel(self.settings_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 340, 141, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.label_3 = QLabel(self.settings_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 440, 131, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"            background-color: rgb(239, 239, 210);\n"
"        }")
        self.bucket_goback_2 = QPushButton(self.settings_page)
        self.bucket_goback_2.setObjectName(u"bucket_goback_2")
        self.bucket_goback_2.setGeometry(QRect(860, 530, 201, 41))
        self.bucket_goback_2.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    \n"
"	\n"
"	background-color: rgb(227, 225, 214);\n"
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
        self.label_15 = QLabel(self.settings_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(470, 210, 251, 91))
        self.label_15.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_16 = QLabel(self.settings_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(470, 310, 251, 91))
        self.label_16.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_17 = QLabel(self.settings_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(470, 410, 251, 91))
        self.label_17.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_18 = QLabel(self.settings_page)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(250, 80, 521, 471))
        self.label_18.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			\n"
"	background-color: rgb(247, 248, 240);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
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
        self.bucket_goback_2.raise_()
        self.buckets = QWidget()
        self.buckets.setObjectName(u"buckets")
        self.title_buckets = QLabel(self.buckets)
        self.title_buckets.setObjectName(u"title_buckets")
        self.title_buckets.setGeometry(QRect(110, 60, 291, 41))
        self.title_buckets.setFont(font)
        self.title_buckets.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.title_buckets.setAlignment(Qt.AlignCenter)
        self.add_bucket_title = QLabel(self.buckets)
        self.add_bucket_title.setObjectName(u"add_bucket_title")
        self.add_bucket_title.setGeometry(QRect(30, 130, 221, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.add_bucket_title.setFont(font1)
        self.add_bucket_title.setStyleSheet(u"background-color: rgb(247, 248, 240);")
        self.add_bucket_title.setAlignment(Qt.AlignCenter)
        self.bucket_input_add = QLineEdit(self.buckets)
        self.bucket_input_add.setObjectName(u"bucket_input_add")
        self.bucket_input_add.setGeometry(QRect(20, 170, 261, 41))
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
        self.bucket_button_add.setGeometry(QRect(290, 170, 201, 41))
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
        self.remove_bucket_title.setGeometry(QRect(-30, 230, 321, 41))
        self.remove_bucket_title.setFont(font1)
        self.remove_bucket_title.setStyleSheet(u"background-color: rgb(247, 248, 240);")
        self.remove_bucket_title.setAlignment(Qt.AlignCenter)
        self.bucket_button_remove = QPushButton(self.buckets)
        self.bucket_button_remove.setObjectName(u"bucket_button_remove")
        self.bucket_button_remove.setGeometry(QRect(290, 280, 201, 41))
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
        self.bucket_goback = QPushButton(self.buckets)
        self.bucket_goback.setObjectName(u"bucket_goback")
        self.bucket_goback.setGeometry(QRect(0, 530, 201, 41))
        self.bucket_goback.setStyleSheet(u"QWidget{\n"
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
        self.cb.setGeometry(QRect(20, 280, 261, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.cb.setFont(font2)
        self.title_buckets_2 = QLabel(self.buckets)
        self.title_buckets_2.setObjectName(u"title_buckets_2")
        self.title_buckets_2.setGeometry(QRect(660, 50, 291, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(22)
        font3.setBold(True)
        self.title_buckets_2.setFont(font3)
        self.title_buckets_2.setAlignment(Qt.AlignCenter)
        self.label_46 = QLabel(self.buckets)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 30, 521, 471))
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
        self.label_47.setGeometry(QRect(540, 30, 521, 471))
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
        self.label_48.setGeometry(QRect(40, 40, 441, 81))
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
        self.title_buckets_3.setGeometry(QRect(650, 60, 291, 41))
        self.title_buckets_3.setFont(font)
        self.title_buckets_3.setStyleSheet(u"background-color: rgb(221, 232, 230);")
        self.title_buckets_3.setAlignment(Qt.AlignCenter)
        self.label_49 = QLabel(self.buckets)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(580, 40, 441, 81))
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
        self.stackedWidget.addWidget(self.buckets)
        self.label_46.raise_()
        self.add_bucket_title.raise_()
        self.bucket_input_add.raise_()
        self.bucket_button_add.raise_()
        self.remove_bucket_title.raise_()
        self.bucket_button_remove.raise_()
        self.bucket_goback.raise_()
        self.cb.raise_()
        self.title_buckets_2.raise_()
        self.label_47.raise_()
        self.label_48.raise_()
        self.title_buckets.raise_()
        self.label_49.raise_()
        self.title_buckets_3.raise_()
        self.installed = QWidget()
        self.installed.setObjectName(u"installed")
        self.stackedWidget.addWidget(self.installed)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.label_27 = QLabel(self.search)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(300, 70, 441, 51))
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
        self.label_28.setGeometry(QRect(30, 50, 1011, 551))
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
        self.search_box_frame.setGeometry(QRect(320, 70, 331, 51))
        self.search_box_frame.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.search_box_frame.setFrameShape(QFrame.NoFrame)
        self.search_box_frame.setFrameShadow(QFrame.Raised)
        self.search_box_frame.setLineWidth(0)
        self.settings_toggle_1_layout_2 = QHBoxLayout(self.search_box_frame)
        self.settings_toggle_1_layout_2.setSpacing(0)
        self.settings_toggle_1_layout_2.setObjectName(u"settings_toggle_1_layout_2")
        self.settings_toggle_1_layout_2.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.search)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(80, 140, 891, 441))
        self.label_29.setStyleSheet(u"QLabel {\n"
"        	background-color: rgb(230, 230, 230);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_30 = QLabel(self.search)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(160, 150, 91, 71))
        self.label_30.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_31 = QLabel(self.search)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(160, 240, 91, 71))
        self.label_31.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_32 = QLabel(self.search)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(160, 320, 91, 71))
        self.label_32.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_33 = QLabel(self.search)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(160, 405, 91, 71))
        self.label_33.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_34 = QLabel(self.search)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(160, 490, 91, 71))
        self.label_34.setStyleSheet(u"QLabel {\n"
"            color: yellow;\n"
"			background-color: rgb(239, 239, 210);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_35 = QLabel(self.search)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(280, 150, 450, 71))
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
        self.label_36.setGeometry(QRect(280, 240, 450, 71))
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
        self.label_37.setGeometry(QRect(280, 322, 450, 71))
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
        self.label_38.setGeometry(QRect(280, 405, 450, 71))
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
        self.label_39.setGeometry(QRect(280, 490, 450, 71))
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
        self.label_40.setGeometry(QRect(770, 150, 131, 71))
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
        self.label_41.setGeometry(QRect(770, 240, 131, 71))
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
        self.label_42.setGeometry(QRect(770, 320, 131, 71))
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
        self.label_43.setGeometry(QRect(770, 405, 131, 71))
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
        self.label_44.setGeometry(QRect(770, 490, 131, 71))
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
        self.label_7.setGeometry(QRect(180, 150, 49, 16))
        self.label_7.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.label_8 = QLabel(self.search)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(440, 150, 91, 16))
        self.label_8.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.label_9 = QLabel(self.search)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(800, 160, 91, 16))
        self.label_9.setStyleSheet(u"background-color: rgb(194, 234, 189);")
        self.label_45 = QLabel(self.search)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(650, 70, 91, 51))
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
        self.app_desc_frame_1.setGeometry(QRect(310, 170, 391, 51))
        self.app_desc_frame_1.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.app_desc_frame_1.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_1.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_1.setLineWidth(0)
        self.app_desc_1_layout = QHBoxLayout(self.app_desc_frame_1)
        self.app_desc_1_layout.setSpacing(0)
        self.app_desc_1_layout.setObjectName(u"app_desc_1_layout")
        self.app_desc_1_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_2 = QFrame(self.search)
        self.app_desc_frame_2.setObjectName(u"app_desc_frame_2")
        self.app_desc_frame_2.setGeometry(QRect(310, 250, 391, 51))
        self.app_desc_frame_2.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.app_desc_frame_2.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_2.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_2.setLineWidth(0)
        self.app_desc_2_layout = QHBoxLayout(self.app_desc_frame_2)
        self.app_desc_2_layout.setSpacing(0)
        self.app_desc_2_layout.setObjectName(u"app_desc_2_layout")
        self.app_desc_2_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_3 = QFrame(self.search)
        self.app_desc_frame_3.setObjectName(u"app_desc_frame_3")
        self.app_desc_frame_3.setGeometry(QRect(310, 330, 391, 51))
        self.app_desc_frame_3.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.app_desc_frame_3.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_3.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_3.setLineWidth(0)
        self.app_desc_3_layout = QHBoxLayout(self.app_desc_frame_3)
        self.app_desc_3_layout.setSpacing(0)
        self.app_desc_3_layout.setObjectName(u"app_desc_3_layout")
        self.app_desc_3_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_4 = QFrame(self.search)
        self.app_desc_frame_4.setObjectName(u"app_desc_frame_4")
        self.app_desc_frame_4.setGeometry(QRect(310, 420, 391, 51))
        self.app_desc_frame_4.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.app_desc_frame_4.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_4.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_4.setLineWidth(0)
        self.app_desc_4_layout = QHBoxLayout(self.app_desc_frame_4)
        self.app_desc_4_layout.setSpacing(0)
        self.app_desc_4_layout.setObjectName(u"app_desc_4_layout")
        self.app_desc_4_layout.setContentsMargins(0, 0, 0, 0)
        self.app_desc_frame_5 = QFrame(self.search)
        self.app_desc_frame_5.setObjectName(u"app_desc_frame_5")
        self.app_desc_frame_5.setGeometry(QRect(310, 500, 391, 51))
        self.app_desc_frame_5.setStyleSheet(u"background-color: rgb(239, 239, 210);")
        self.app_desc_frame_5.setFrameShape(QFrame.NoFrame)
        self.app_desc_frame_5.setFrameShadow(QFrame.Raised)
        self.app_desc_frame_5.setLineWidth(0)
        self.app_desc_5_layout = QHBoxLayout(self.app_desc_frame_5)
        self.app_desc_5_layout.setSpacing(0)
        self.app_desc_5_layout.setObjectName(u"app_desc_5_layout")
        self.app_desc_5_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_1 = QFrame(self.search)
        self.app_install_frame_1.setObjectName(u"app_install_frame_1")
        self.app_install_frame_1.setGeometry(QRect(780, 160, 101, 51))
        self.app_install_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_1.setStyleSheet(u"background-color: rgb(194, 234, 189);")
        self.app_install_frame_1.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_1.setFrameShadow(QFrame.Raised)
        self.app_install_frame_1.setLineWidth(0)
        self.app_install_1_layout = QHBoxLayout(self.app_install_frame_1)
        self.app_install_1_layout.setSpacing(0)
        self.app_install_1_layout.setObjectName(u"app_install_1_layout")
        self.app_install_1_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_2 = QFrame(self.search)
        self.app_install_frame_2.setObjectName(u"app_install_frame_2")
        self.app_install_frame_2.setGeometry(QRect(780, 250, 101, 51))
        self.app_install_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_2.setStyleSheet(u"background-color: rgb(194, 234, 189);")
        self.app_install_frame_2.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_2.setFrameShadow(QFrame.Raised)
        self.app_install_frame_2.setLineWidth(0)
        self.app_install_2_layout = QHBoxLayout(self.app_install_frame_2)
        self.app_install_2_layout.setSpacing(0)
        self.app_install_2_layout.setObjectName(u"app_install_2_layout")
        self.app_install_2_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_3 = QFrame(self.search)
        self.app_install_frame_3.setObjectName(u"app_install_frame_3")
        self.app_install_frame_3.setGeometry(QRect(780, 330, 101, 51))
        self.app_install_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_3.setStyleSheet(u"background-color: rgb(194, 234, 189);")
        self.app_install_frame_3.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_3.setFrameShadow(QFrame.Raised)
        self.app_install_frame_3.setLineWidth(0)
        self.app_install_3_layout = QHBoxLayout(self.app_install_frame_3)
        self.app_install_3_layout.setSpacing(0)
        self.app_install_3_layout.setObjectName(u"app_install_3_layout")
        self.app_install_3_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_4 = QFrame(self.search)
        self.app_install_frame_4.setObjectName(u"app_install_frame_4")
        self.app_install_frame_4.setGeometry(QRect(780, 410, 101, 51))
        self.app_install_frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_4.setStyleSheet(u"background-color: rgb(194, 234, 189);")
        self.app_install_frame_4.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_4.setFrameShadow(QFrame.Raised)
        self.app_install_frame_4.setLineWidth(0)
        self.app_install_4_layout = QHBoxLayout(self.app_install_frame_4)
        self.app_install_4_layout.setSpacing(0)
        self.app_install_4_layout.setObjectName(u"app_install_4_layout")
        self.app_install_4_layout.setContentsMargins(0, 0, 0, 0)
        self.app_install_frame_5 = QFrame(self.search)
        self.app_install_frame_5.setObjectName(u"app_install_frame_5")
        self.app_install_frame_5.setGeometry(QRect(780, 500, 101, 51))
        self.app_install_frame_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.app_install_frame_5.setStyleSheet(u"background-color: rgb(194, 234, 189);")
        self.app_install_frame_5.setFrameShape(QFrame.NoFrame)
        self.app_install_frame_5.setFrameShadow(QFrame.Raised)
        self.app_install_frame_5.setLineWidth(0)
        self.app_install_5_layout = QHBoxLayout(self.app_install_frame_5)
        self.app_install_5_layout.setSpacing(0)
        self.app_install_5_layout.setObjectName(u"app_install_5_layout")
        self.app_install_5_layout.setContentsMargins(0, 0, 0, 0)
        self.app_search_frame = QFrame(self.search)
        self.app_search_frame.setObjectName(u"app_search_frame")
        self.app_search_frame.setGeometry(QRect(660, 80, 71, 31))
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
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add or remove scoop buckets/apps", None))
        self.label_25.setText("")
        self.label_26.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Faster Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Use Download Manager", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Some other setting", None))
        self.bucket_goback_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.title_buckets.setText(QCoreApplication.translate("MainWindow", u"Manage Buckets", None))
        self.add_bucket_title.setText(QCoreApplication.translate("MainWindow", u"Add Bucket", None))
        self.bucket_input_add.setText(QCoreApplication.translate("MainWindow", u"Bucket Name / URL", None))
#if QT_CONFIG(tooltip)
        self.bucket_button_add.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>test</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bucket_button_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_bucket_title.setText(QCoreApplication.translate("MainWindow", u"Remove Bucket", None))
        self.bucket_button_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.bucket_goback.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.title_buckets_2.setText(QCoreApplication.translate("MainWindow", u"Manage Buckets", None))
        self.label_46.setText("")
        self.label_47.setText("")
        self.label_48.setText("")
        self.title_buckets_3.setText(QCoreApplication.translate("MainWindow", u"Manage Apps", None))
        self.label_49.setText("")
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
    # retranslateUi


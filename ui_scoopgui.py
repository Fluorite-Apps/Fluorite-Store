# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scoopguiPOYHeL.ui'
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
    QScrollArea, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

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
        self.search_layout.setGeometry(QRect(50, 230, 220, 145))
        self.search_layout.setFrameShape(QFrame.NoFrame)
        self.search_layout.setFrameShadow(QFrame.Raised)
        self.search_layout.setLineWidth(0)
        self.enter_search_layout = QHBoxLayout(self.search_layout)
        self.enter_search_layout.setSpacing(0)
        self.enter_search_layout.setObjectName(u"enter_search_layout")
        self.enter_search_layout.setContentsMargins(0, 0, 0, 0)
        self.manage_apps_frame = QFrame(self.home)
        self.manage_apps_frame.setObjectName(u"manage_apps_frame")
        self.manage_apps_frame.setGeometry(QRect(300, 230, 220, 145))
        self.manage_apps_frame.setFrameShape(QFrame.NoFrame)
        self.manage_apps_frame.setFrameShadow(QFrame.Raised)
        self.manage_apps_frame.setLineWidth(0)
        self.enter_manage_apps_layout = QHBoxLayout(self.manage_apps_frame)
        self.enter_manage_apps_layout.setSpacing(0)
        self.enter_manage_apps_layout.setObjectName(u"enter_manage_apps_layout")
        self.enter_manage_apps_layout.setContentsMargins(0, 0, 0, 0)
        self.manage_buckets_frame = QFrame(self.home)
        self.manage_buckets_frame.setObjectName(u"manage_buckets_frame")
        self.manage_buckets_frame.setGeometry(QRect(550, 230, 220, 145))
        self.manage_buckets_frame.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame.setLineWidth(0)
        self.enter_manage_buckets_layout = QHBoxLayout(self.manage_buckets_frame)
        self.enter_manage_buckets_layout.setSpacing(0)
        self.enter_manage_buckets_layout.setObjectName(u"enter_manage_buckets_layout")
        self.enter_manage_buckets_layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.home)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(-20, 80, 1101, 41))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(22)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.settings_frame = QFrame(self.home)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setGeometry(QRect(800, 230, 251, 145))
        self.settings_frame.setFrameShape(QFrame.NoFrame)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.settings_frame.setLineWidth(0)
        self.settings_page_layout = QHBoxLayout(self.settings_frame)
        self.settings_page_layout.setSpacing(0)
        self.settings_page_layout.setObjectName(u"settings_page_layout")
        self.settings_page_layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.home)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.manage_buckets_frame_2 = QFrame(self.settings_page)
        self.manage_buckets_frame_2.setObjectName(u"manage_buckets_frame_2")
        self.manage_buckets_frame_2.setGeometry(QRect(470, 220, 131, 71))
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
        self.manage_buckets_frame_3.setGeometry(QRect(470, 320, 131, 71))
        self.manage_buckets_frame_3.setFrameShape(QFrame.NoFrame)
        self.manage_buckets_frame_3.setFrameShadow(QFrame.Raised)
        self.manage_buckets_frame_3.setLineWidth(0)
        self.settings_toggle_2_layout = QHBoxLayout(self.manage_buckets_frame_3)
        self.settings_toggle_2_layout.setSpacing(0)
        self.settings_toggle_2_layout.setObjectName(u"settings_toggle_2_layout")
        self.settings_toggle_2_layout.setContentsMargins(0, 0, 0, 0)
        self.manage_buckets_frame_4 = QFrame(self.settings_page)
        self.manage_buckets_frame_4.setObjectName(u"manage_buckets_frame_4")
        self.manage_buckets_frame_4.setGeometry(QRect(470, 420, 131, 71))
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
        font1 = QFont()
        font1.setPointSize(16)
        self.title_2.setFont(font1)
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
        self.stackedWidget.addWidget(self.settings_page)
        self.buckets = QWidget()
        self.buckets.setObjectName(u"buckets")
        self.title_buckets = QLabel(self.buckets)
        self.title_buckets.setObjectName(u"title_buckets")
        self.title_buckets.setGeometry(QRect(-10, 40, 1081, 41))
        self.title_buckets.setFont(font)
        self.title_buckets.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.buckets)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 100, 301, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 299, 399))
        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 0, 291, 401))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.list_buckets_layout = QHBoxLayout(self.frame_5)
        self.list_buckets_layout.setSpacing(0)
        self.list_buckets_layout.setObjectName(u"list_buckets_layout")
        self.list_buckets_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.add_bucket_title = QLabel(self.buckets)
        self.add_bucket_title.setObjectName(u"add_bucket_title")
        self.add_bucket_title.setGeometry(QRect(310, 100, 771, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.add_bucket_title.setFont(font2)
        self.add_bucket_title.setAlignment(Qt.AlignCenter)
        self.list_bucket_title = QLabel(self.buckets)
        self.list_bucket_title.setObjectName(u"list_bucket_title")
        self.list_bucket_title.setGeometry(QRect(0, 50, 311, 41))
        self.list_bucket_title.setFont(font2)
        self.list_bucket_title.setAlignment(Qt.AlignCenter)
        self.bucket_input_add = QLineEdit(self.buckets)
        self.bucket_input_add.setObjectName(u"bucket_input_add")
        self.bucket_input_add.setGeometry(QRect(350, 150, 421, 41))
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
        self.bucket_button_add.setGeometry(QRect(820, 150, 201, 41))
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
        self.remove_bucket_title.setGeometry(QRect(310, 300, 771, 41))
        self.remove_bucket_title.setFont(font2)
        self.remove_bucket_title.setAlignment(Qt.AlignCenter)
        self.bucket_button_remove = QPushButton(self.buckets)
        self.bucket_button_remove.setObjectName(u"bucket_button_remove")
        self.bucket_button_remove.setGeometry(QRect(820, 350, 201, 41))
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
        self.cb.setGeometry(QRect(350, 350, 421, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.cb.setFont(font3)
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
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.title_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Faster Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Use Download Manager", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Some other setting", None))
        self.bucket_goback_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.title_buckets.setText(QCoreApplication.translate("MainWindow", u"Manage Buckets", None))
        self.add_bucket_title.setText(QCoreApplication.translate("MainWindow", u"Add Bucket", None))
        self.list_bucket_title.setText(QCoreApplication.translate("MainWindow", u"Bucket List", None))
        self.bucket_input_add.setText(QCoreApplication.translate("MainWindow", u"Bucket Name / URL", None))
#if QT_CONFIG(tooltip)
        self.bucket_button_add.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>test</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bucket_button_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_bucket_title.setText(QCoreApplication.translate("MainWindow", u"Remove Bucket", None))
        self.bucket_button_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.bucket_goback.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi


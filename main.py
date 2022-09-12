import sys

from ui_scoopgui import *

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
from os.path import exists

from py_toggle import *

from Second_PushButton import *

import resource_file_qt_rc

###################################################################################################################
#####   https://tenor.com/view/calculating-puzzled-math-confused-confused-look-gif-14677181                    ####

#####   U S E -  C O M M E N TS txog - literally me when i was trying to understand spaghetti without comments     #####

#####   https://tenor.com/view/calculating-puzzled-math-confused-confused-look-gif-14677181                    ###
###################################################################################################################

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None , *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs, parent=parent)
        self.setupUi(self)
        self.search_page_button = QPushButton('Search', parent=self)
        self.manage_buckets_button = QtWidgets.QPushButton('Buckets', parent=self)

        # loading splashscreen
        # self.stackedWidget.setCurrentWidget(self.splashscreen)


        ###################################################################################################################
        # RECOMMENDED APPS PAGE
        ###################################################################################################################

        # making widget and adding to layout
        self.go_recommended_apps_page_button = QtWidgets.QPushButton('Starred', parent=self)

        self.enter_recommended_apps_frame.addWidget(self.go_recommended_apps_page_button, Qt.AlignCenter, Qt.AlignCenter)

        # attaching to function
        self.go_recommended_apps_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.recommended_apps_page_1))

        # install buttons - page 1
        self.recc_app_install_button_1 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_1.setMinimumHeight(71)
        self.recc_app_install_button_1.setFixedWidth(131)

        self.recc_app_install_button_2 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_2.setMinimumHeight(71)
        self.recc_app_install_button_2.setFixedWidth(131)

        self.recc_app_install_button_3 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_3.setMinimumHeight(71)
        self.recc_app_install_button_3.setFixedWidth(131)

        self.recc_app_install_button_4 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_4.setMinimumHeight(71)
        self.recc_app_install_button_4.setFixedWidth(131)

        self.recc_app_install_button_5 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_5.setMinimumHeight(71)
        self.recc_app_install_button_5.setFixedWidth(131)

        # install buttons - page 2
        self.recc_app_install_button_6 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_6.setMinimumHeight(71)
        self.recc_app_install_button_6.setFixedWidth(131)

        self.recc_app_install_button_7 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_7.setMinimumHeight(71)
        self.recc_app_install_button_7.setFixedWidth(131)

        self.recc_app_install_button_8 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_8.setMinimumHeight(71)
        self.recc_app_install_button_8.setFixedWidth(131)

        self.recc_app_install_button_9 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_9.setMinimumHeight(71)
        self.recc_app_install_button_9.setFixedWidth(131)

        self.recc_app_install_button_10 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_10.setMinimumHeight(71)
        self.recc_app_install_button_10.setFixedWidth(131)

        # install buttons - page 3
        self.recc_app_install_button_11 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_11.setMinimumHeight(71)
        self.recc_app_install_button_11.setFixedWidth(131)

        self.recc_app_install_button_12 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_12.setMinimumHeight(71)
        self.recc_app_install_button_12.setFixedWidth(131)

        self.recc_app_install_button_13 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_13.setMinimumHeight(71)
        self.recc_app_install_button_13.setFixedWidth(131)

        self.recc_app_install_button_14 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_14.setMinimumHeight(71)
        self.recc_app_install_button_14.setFixedWidth(131)

        self.recc_app_install_button_15 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_15.setMinimumHeight(71)
        self.recc_app_install_button_15.setFixedWidth(131)

        # install buttons - page 4
        self.recc_app_install_button_16 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_16.setMinimumHeight(71)
        self.recc_app_install_button_16.setFixedWidth(131)

        self.recc_app_install_button_17 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_17.setMinimumHeight(71)
        self.recc_app_install_button_17.setFixedWidth(131)

        self.recc_app_install_button_18 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_18.setMinimumHeight(71)
        self.recc_app_install_button_18.setFixedWidth(131)

        self.recc_app_install_button_19 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_19.setMinimumHeight(71)
        self.recc_app_install_button_19.setFixedWidth(131)

        self.recc_app_install_button_20 = custompushbutton('Install', parent=self)
        self.recc_app_install_button_20.setMinimumHeight(71)
        self.recc_app_install_button_20.setFixedWidth(131)


        # attaching page 1 buttons to layouts
        self.recc_app_install_layout_1.addWidget(self.recc_app_install_button_1, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_2.addWidget(self.recc_app_install_button_2, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_3.addWidget(self.recc_app_install_button_3, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_4.addWidget(self.recc_app_install_button_4, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_5.addWidget(self.recc_app_install_button_5, Qt.AlignCenter, Qt.AlignCenter)

        # attaching page 1 buttons to layouts
        self.recc_app_install_layout_6.addWidget(self.recc_app_install_button_6, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_7.addWidget(self.recc_app_install_button_7, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_8.addWidget(self.recc_app_install_button_8, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_9.addWidget(self.recc_app_install_button_9, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_10.addWidget(self.recc_app_install_button_10, Qt.AlignCenter, Qt.AlignCenter)

        # attaching page 2 buttons to layouts
        self.recc_app_install_layout_11.addWidget(self.recc_app_install_button_11, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_12.addWidget(self.recc_app_install_button_12, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_13.addWidget(self.recc_app_install_button_13, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_14.addWidget(self.recc_app_install_button_14, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_15.addWidget(self.recc_app_install_button_15, Qt.AlignCenter, Qt.AlignCenter)

        # attaching page 3 buttons to layouts
        self.recc_app_install_layout_16.addWidget(self.recc_app_install_button_16, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_17.addWidget(self.recc_app_install_button_17, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_18.addWidget(self.recc_app_install_button_18, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_19.addWidget(self.recc_app_install_button_19, Qt.AlignCenter, Qt.AlignCenter)
        self.recc_app_install_layout_20.addWidget(self.recc_app_install_button_20, Qt.AlignCenter, Qt.AlignCenter)

        # functions for installing recommended apps on button click

        def install_recc_app_1():
            # toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install hwinfo']
            # process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            #                                 universal_newlines=True)
            print ("unfortunately portmaster isn't on scoop yet, so i'll have to find some other way to install this later. Coming soon..")

        def install_recc_app_2():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install fluent-reader']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_3():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install flameshot']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_4():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install ludusavi']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_5():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install compactgui']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_6():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install peazip']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_7():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install librewolf']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_8():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install freetube']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_9():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install geekuninstaller']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_10():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install simplewall']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_11():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install sandboxie-plus-np']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_12():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install playnite']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_13():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install crystaldiskinfo']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_14():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install hwinfo']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_15():
            # toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install hwinfo']
            # process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            #                                 universal_newlines=True)
            print(
                "unfortunately OCCT isn't on scoop yet, so i'll have to find some other way to install this later. Coming soon..")

        def install_recc_app_16():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install shutup10']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_17():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install mpv']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_18():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install tabby']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_19():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install eartrumpet']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)
        def install_recc_app_20():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install ryujinx']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)

        # launching install functions in seperate thread = no gui hang
        def thread_install_recc_app_1():
            t = Thread(target=install_recc_app_1)
            t.daemon = True
            t.start()

        def thread_install_recc_app_2():
            t = Thread(target=install_recc_app_2)
            t.daemon = True
            t.start()

        def thread_install_recc_app_3():
            t = Thread(target=install_recc_app_3)
            t.daemon = True
            t.start()

        def thread_install_recc_app_4():
            t = Thread(target=install_recc_app_4)
            t.daemon = True
            t.start()

        def thread_install_recc_app_5():
            t = Thread(target=install_recc_app_5)
            t.daemon = True
            t.start()

        def thread_install_recc_app_6():
            t = Thread(target=install_recc_app_6)
            t.daemon = True
            t.start()

        def thread_install_recc_app_7():
            t = Thread(target=install_recc_app_7)
            t.daemon = True
            t.start()

        def thread_install_recc_app_8():
            t = Thread(target=install_recc_app_8)
            t.daemon = True
            t.start()

        def thread_install_recc_app_9():
            t = Thread(target=install_recc_app_9)
            t.daemon = True
            t.start()

        def thread_install_recc_app_10():
            t = Thread(target=install_recc_app_10)
            t.daemon = True
            t.start()

        def thread_install_recc_app_11():
            t = Thread(target=install_recc_app_11)
            t.daemon = True
            t.start()

        def thread_install_recc_app_12():
            t = Thread(target=install_recc_app_12)
            t.daemon = True
            t.start()

        def thread_install_recc_app_13():
            t = Thread(target=install_recc_app_13)
            t.daemon = True
            t.start()

        def thread_install_recc_app_14():
            t = Thread(target=install_recc_app_14)
            t.daemon = True
            t.start()

        def thread_install_recc_app_15():
            t = Thread(target=install_recc_app_15)
            t.daemon = True
            t.start()

        def thread_install_recc_app_16():
            t = Thread(target=install_recc_app_16)
            t.daemon = True
            t.start()

        def thread_install_recc_app_17():
            t = Thread(target=install_recc_app_17)
            t.daemon = True
            t.start()

        def thread_install_recc_app_18():
            t = Thread(target=install_recc_app_18)
            t.daemon = True
            t.start()

        def thread_install_recc_app_19():
            t = Thread(target=install_recc_app_19)
            t.daemon = True
            t.start()

        def thread_install_recc_app_20():
            t = Thread(target=install_recc_app_20)
            t.daemon = True
            t.start()

        def do_nothing():
            print ("coming soon")

        # attaching all 20 to functions
        # currently do nothing
        self.recc_app_install_button_1.clicked.connect(lambda: thread_install_recc_app_1())
        self.recc_app_install_button_2.clicked.connect(lambda: thread_install_recc_app_2())
        self.recc_app_install_button_3.clicked.connect(lambda: thread_install_recc_app_3())
        self.recc_app_install_button_4.clicked.connect(lambda: thread_install_recc_app_4())
        self.recc_app_install_button_5.clicked.connect(lambda: thread_install_recc_app_5())
        self.recc_app_install_button_6.clicked.connect(lambda: thread_install_recc_app_6())
        self.recc_app_install_button_7.clicked.connect(lambda: thread_install_recc_app_7())
        self.recc_app_install_button_8.clicked.connect(lambda: thread_install_recc_app_8())
        self.recc_app_install_button_9.clicked.connect(lambda: thread_install_recc_app_9())
        self.recc_app_install_button_10.clicked.connect(lambda: thread_install_recc_app_10())
        self.recc_app_install_button_11.clicked.connect(lambda: thread_install_recc_app_11())
        self.recc_app_install_button_12.clicked.connect(lambda: thread_install_recc_app_12())
        self.recc_app_install_button_13.clicked.connect(lambda: thread_install_recc_app_13())
        self.recc_app_install_button_14.clicked.connect(lambda: thread_install_recc_app_14())
        self.recc_app_install_button_15.clicked.connect(lambda: thread_install_recc_app_15())
        self.recc_app_install_button_16.clicked.connect(lambda: thread_install_recc_app_16())
        self.recc_app_install_button_17.clicked.connect(lambda: thread_install_recc_app_17())
        self.recc_app_install_button_18.clicked.connect(lambda: thread_install_recc_app_18())
        self.recc_app_install_button_19.clicked.connect(lambda: thread_install_recc_app_19())
        self.recc_app_install_button_20.clicked.connect(lambda: thread_install_recc_app_20())

        ###################################################################################################################
        # BUCKETS AND APPS PAGE
        ###################################################################################################################
        self.update_all_apps_button = QtWidgets.QPushButton('update', parent=self)

        # adding widgets to layout
        self.update_all_apps_layout.addWidget(self.update_all_apps_button, Qt.AlignCenter, Qt.AlignCenter)

        # updating all apps function
        self.update_all_apps_button.clicked.connect(self.update_all_apps_thread)

        # settings page
        self.settings_page_button = QtWidgets.QPushButton('Settings', parent=self)
        self.settings_page_layout.addWidget(self.settings_page_button, Qt.AlignCenter, Qt.AlignCenter)
        self.settings_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.settings_page) )


        self.enter_search_layout.addWidget(self.search_page_button, Qt.AlignCenter, Qt.AlignCenter)
        self.enter_manage_buckets_layout.addWidget(self.manage_buckets_button, Qt.AlignCenter, Qt.AlignCenter)
        self.search_page_button.clicked.connect(self.goSearch)
        self.manage_buckets_button.clicked.connect(self.goBuckets)

        ###################################################################################################################
        # SETTINGS PAGE
        ###################################################################################################################

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

        # adding widgets to layout
        self.settings_toggle_1_layout.addWidget(self.thing, Qt.AlignCenter, Qt.AlignCenter)
        self.settings_toggle_2_layout.addWidget(self.another_thing, Qt.AlignCenter, Qt.AlignCenter)
        self.settings_toggle_3_layout.addWidget(self.a_thing, Qt.AlignCenter, Qt.AlignCenter)

        def install_aria2c():
            toggle_command_1 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install aria2c']
            process_result = subprocess.run(toggle_command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)

        def install_scoop_search():
            toggle_command_2 = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop install scoop-search']
            process_result = subprocess.run(toggle_command_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            universal_newlines=True)

        # checking if toggle has been toggled, looped on thread
        # loop ends if ticked, only runs if never ran before

        # time.sleep is necessary otherwise the 3 checks running concurrently hogs system resources,
        # set to 1 check per sec for each of the 3

        def continuous_checking_downloadmanager_toggle_status():
            while True:
                time.sleep(1)
                if self.thing.isChecked() == True:
                    # checking if has_ran_before_one exists, if not runs and creates
                    if exists(has_ran_before_one):
                        # install aria2c in a seperate thread
                        t = Thread(target=install_aria2c)
                        t.daemon = True
                        t.start()

                        # making has_ran_before_one file
                        file_one = open(r"has_ran_before_one", "w")
                        file_one.write(" ")
                        break
                    else:
                        print ("already ran before, skipping")
                        break

        def continuous_checking_fastsearch_toggle_status():
            while True:
                time.sleep(1)
                if self.a_thing.isChecked() == True:
                    # checking if has_ran_before_two exists, if not runs and creates
                    if exists(has_ran_before_two):
                        # install scoop-search in a seperate thread
                        t = Thread(target=install_scoop_search)
                        t.daemon = True
                        t.start()

                        # making has_ran_before_two file
                        file_two = open(r"has_ran_before_two", "w")
                        file_two.write(" ")
                        break
                    else:
                        print("already ran before, skipping")
                        break

        def continuous_checking_other_toggle_status():
            while True:
                time.sleep(1)
                if self.another_thing.isChecked() == True:
                    # placeholder for future 3rd toggle
                    print ("thing 3")
                    break



        # concurrently run 3 toggle checks when opening settings
        t = Thread(target=continuous_checking_downloadmanager_toggle_status)
        t.daemon = True
        t.start()

        t = Thread(target=continuous_checking_fastsearch_toggle_status)
        t.daemon = True
        t.start()

        t = Thread(target=continuous_checking_other_toggle_status)
        t.daemon = True
        t.start()

        # self.stateTooltip = None
        with open('resource/pushbutton/push_button.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())


    # update all apps
    def update_all_apps_function(self):
        update_all_apps_powershell = [POWERSHELL_PATH, '-ExecutionPolicy', 'Unrestricted', 'scoop update *']
        update_all_apps_powershell2 = subprocess.run(update_all_apps_powershell, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        universal_newlines=True)

    def update_all_apps_thread(self):
        t = Thread(target=self.update_all_apps_function)
        t.daemon = True
        t.start()

    def goSearch(self):
        self.stackedWidget.setCurrentWidget(self.search)

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

            # return to homepage
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


# dedicated gorilla function
def dedicated_gorilla_function():
    while True:
        time.sleep(1)
        print ("gorilla")

t = Thread(target=dedicated_gorilla_function)
t.daemon = True
t.start()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Scoop GUI')
my_pixmap = QPixmap("scoopicon.ico")
my_icon = QIcon(my_pixmap)
window.setWindowIcon(my_icon)
window.show()
app.exec()
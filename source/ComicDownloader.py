# -*- coding: utf-8 -*-
"""
more information cam be found at usage()

how to make it an executable file:
    pyinstaller --onefile --windowed --icon=./Images/icons8-pluto-dwarf-planet-48.png ComicDownloader.py --hidden-import=queue
"""

print("[INFO] Initializing...")
import time
time_start = time.time()

from urllib.parse import urlparse, quote, unquote
from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.parse import quote, urlparse
from selenium import webdriver
from natsort import natsorted
from bs4 import BeautifulSoup
from PIL import Image
import subprocess
import threading
import traceback
import requests
import warnings
import socket
import shutil
import getopt
import glob
import json
import sys
import os
import re

RETURN_ZERO = 0
ERR_NO_SEARCH_RESULT = -1
ERR_SOURCE_NOT_RECOGNIZED = -2
ERR_OPTION_NOT_RECOGNIZED = -3
ERR_TOO_MANY_SPACE_IN_QUERY = -4
ERR_NO_QUERY_GIVEN = -5
ERR_WHILE_REQUITING_DATA = -6
ERR_NO_EPISODE_IN_COMIC = -7
ERR_NO_ARGUMENT_PASSED = -8
ERR_NOT_CONNECTED_TO_INTERNET = -9
ERR_FEATURE_NOT_READY = -10
ERR_INVALID_URL = -1
ERR_CANNOT_CONNECT_TO_SERVER = -4
ERR_UNDEFINED = -5
ERR_RSS = -7
ERR_COOKIE = -8
ERR_DOWNLOAD = -9
ERR_NO_EPISODE = -10
ERR_NO_IMAGES = -11
ERR_WHILE_STITCHING_IMAGES = -12
ERR_SOURCE_IS_NOT_A_NUMBER = -14
ERR_SOURCE_NOT_GIVEN = -15

COMIC_TYPE_NAVER = 0
COMIC_TYPE_NAVER_BEST_CHALLENGE = 1
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3
COMIC_TYPE_KAKAO = 4


class UiComicDownloaderWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiComicDownloaderWindow, self).__init__()
        self.msg_error = ""
        self.width, self.height = 800, 500
        self.y_pos = int((screen_height - self.height) / 2)
        self.x_pos = int((screen_width - self.width) / 2)
        
        self.setObjectName("ComicDownloaderWindow")
        self.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setWindowTitle("Comic Downloader v4-alpha")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/icons8-pluto-dwarf-planet-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.tab_widget_main = QtWidgets.QTabWidget(self.centralWidget)
        self.tab_widget_main.setGeometry(QtCore.QRect(0, 0, 800, 490))
        self.tab_widget_main.setObjectName("tab_widget_main")
        self.tab_search = QtWidgets.QWidget()
        self.tab_search.setObjectName("tab_search")
        #
        # Scroll Area
        #
        self.scroll_area_results = QtWidgets.QScrollArea(self.tab_search)
        self.scroll_area_results.setGeometry(QtCore.QRect(-1, 60, 801, 390))
        self.scroll_area_results.setWidgetResizable(True)
        
        self.widget_results_scroll = QtWidgets.QWidget()
        self.widget_results_scroll.setGeometry(QtCore.QRect(0, 0, 799, 388))
        self.widget_results_scroll.setObjectName("widget_results_scroll")
        self.scroll_area_results.setWidget(self.widget_results_scroll)
        self.v_box_layout_results = QtWidgets.QVBoxLayout(self.widget_results_scroll)
        self.scroll_area_results_all = QtWidgets.QVBoxLayout()
        self.scroll_area_results_all.addWidget(self.scroll_area_results)
        self.scroll_area_results.setObjectName("scroll_area_results")
        
        self.text_edit_search = SearchBox(self.tab_search)
        self.text_edit_search.setGeometry(QtCore.QRect(150, 0, 600, 30))
        self.text_edit_search.setObjectName("text_edit_search")
        
        self.combo_box_source = QtWidgets.QComboBox(self.tab_search)
        self.combo_box_source.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.combo_box_source.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combo_box_source.setObjectName("combo_box_source")
        self.label_error = QtWidgets.QLabel(self.tab_search)
        self.label_error.setGeometry(QtCore.QRect(150, 30, 651, 30))
        self.label_error.setObjectName("label_error")
        self.btn_push_search = QtWidgets.QPushButton(self.tab_search)
        self.btn_push_search.setGeometry(QtCore.QRect(750, 0, 50, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_push_search.sizePolicy().hasHeightForWidth())
        self.btn_push_search.setSizePolicy(sizePolicy)
        self.btn_push_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/icons8-search-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_push_search.setIcon(icon1)
        self.btn_push_search.setIconSize(QtCore.QSize(24, 24))
        self.btn_push_search.setFlat(False)
        self.btn_push_search.setObjectName("btn_push_search")
        self.tab_widget_main.addTab(self.tab_search, "")
        self.tab_downloads = QtWidgets.QWidget()
        self.tab_downloads.setObjectName("tab_downloads")
        self.scroll_area_downloads = QtWidgets.QScrollArea(self.tab_downloads)
        self.scroll_area_downloads.setGeometry(QtCore.QRect(0, 0, 800, 460))
        self.scroll_area_downloads.setFrameShape(QtWidgets.QFrame.VLine)
        self.scroll_area_downloads.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scroll_area_downloads.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area_downloads.setWidgetResizable(True)
        self.scroll_area_downloads.setObjectName("scroll_area_downloads")
        self.scroll_area_widget_contents_downloads = QtWidgets.QWidget()
        self.scroll_area_widget_contents_downloads.setGeometry(QtCore.QRect(0, 0, 798, 458))
        self.scroll_area_widget_contents_downloads.setObjectName("scroll_area_widget_contents_downloads")
        self.scroll_area_downloads.setWidget(self.scroll_area_widget_contents_downloads)
        self.tab_widget_main.addTab(self.tab_downloads, "")
        self.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_tools = QtWidgets.QMenu(self.menubar)
        self.menu_tools.setObjectName("menu_tools")
        self.setMenuBar(self.menubar)
        self.action_about = QtWidgets.QAction(self)
        self.action_about.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_about.setObjectName("action_about")
        self.action_log = QtWidgets.QAction(self)
        self.action_log.setObjectName("action_log")
        self.menu_tools.addAction(self.action_log)
        self.menu_tools.addAction(self.action_about)
        self.menubar.addAction(self.menu_tools.menuAction())
        
        self.retranslateUi()
        self.tab_widget_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.btn_push_search.clicked.connect(self.btn_push_search_click)
        self.action_log.triggered.connect(self.log_click)
        self.action_about.triggered.connect(self.about_click)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.combo_box_source.addItem("Funbe")
        self.combo_box_source.addItem("Naver")
        self.combo_box_source.addItem("Daum")
        self.combo_box_source.addItem("Kakao")

        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_search), _translate("ComicDownloaderWindow", "Search"))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_downloads), _translate("ComicDownloaderWindow", "Downloads"))
        self.menu_tools.setTitle(_translate("ComicDownloaderWindow", "Tools"))
        self.action_about.setText(_translate("ComicDownloaderWindow", "About"))
        self.action_log.setText(_translate("ComicDownloaderWindow", "Show Log"))
        
    def btn_push_search_click(self):
        print(self.text_edit_search.toPlainText())
        print(self.combo_box_source.currentIndex())
        for i in range(15):
            self.v_box_layout_results.addWidget(self.createLayout_group())
        
    def createLayout_group(self):
        sgroupbox = QtWidgets.QGroupBox(self)
        
        layout_groupbox = QtWidgets.QVBoxLayout(sgroupbox)
        for i in element_list:
            item = QtWidgets.QLabel(i, sgroupbox)
            layout_groupbox.addWidget(item)
        return sgroupbox
        
    def about_click(self):
        text = "<center>" \
               "<h1>Comic Downloader</h1>" \
               "</center>" \
               "Version: v4-alpha<br>" \
               "Release date: 2019 September 27<br>" \
               "Copyright: CC-BY 4.0 &copy; AnonymousPomp<br>" \
               "Email: anonymouspomp@gmail.com<br>" \
               "<br><br>" \
               "Source code available on github:<br>" \
               "https://github.com/AnonymousPomp/Comic-Downloader<br>" \
        
        QtWidgets.QMessageBox.about(self, "About", text)
        
    def log_click(self):
        info = QtWidgets.QMessageBox()
        info.setWindowTitle("Log")
        info.setText(self.msg_error)
        info.exec_()


class SearchBox(QtWidgets.QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            ComicDownloader.btn_push_search_click()
        else:
            super().keyPressEvent(qKeyEvent)


if __name__ == "__main__":
    import sys
    element_list = ["Title", "Thumbnail", "Author"]
    
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    screen_resolution = app.desktop().screenGeometry()
    screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
    
    ComicDownloader = UiComicDownloaderWindow()
    ComicDownloader.show()
    sys.exit(app.exec_())

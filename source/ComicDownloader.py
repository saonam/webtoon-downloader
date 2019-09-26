#!/usr/bin/env python3
# coding: utf-8
"""
compile:
    pyinstaller --onefile --icon=./Images/icons8_Pluto_Dwarf_Planet_3.ico ComicDownloader.py
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

app = QtWidgets.QApplication(sys.argv)
screen_resolution = app.desktop().screenGeometry()
screen_width, screen_height = screen_resolution.width(), screen_resolution.height()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.width, self.height = 800, 500
        self.y_pos = int((screen_height-self.height)/2)
        self.x_pos = int((screen_width-self.width)/2)
        self.setWindowTitle("Comic Downloader v4-alpha")
        self.setWindowIcon(QtGui.QIcon("./Images/icons8_Pluto_Dwarf_Planet_3.ico"))
        self.setGeometry(self.x_pos, self.y_pos, self.width, self.height)
        self.initialize()
        self.show()

    def initialize(self):
        btn_push_download = QtWidgets.QPushButton("Download", self)
        btn_push_download.clicked.connect(self.btn_push_download_click)
        btn_push_download.show()

    @staticmethod
    def btn_push_download_click():
        print("downloading...")


GUI = Window()
sys.exit(app.exec_())

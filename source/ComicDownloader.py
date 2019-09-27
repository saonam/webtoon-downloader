# -*- coding: utf-8 -*-
"""
Form implementation generated from reading ui file 'ComicDownloader.ui'
Created by: PyQt5 UI code generator 5.13.1

Edited by: Anonymous Pomp (anonymouspomp@gmail.com)

Commands:
    compile: pyinstaller --onefile --icon=./Images/icons8-pluto-dwarf-planet-48.png ComicDownloader.py
"""

from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.scroll_area_results_all = QtWidgets.QVBoxLayout(self)
        self.scroll_area_results_all.addWidget(self.scroll_area_results)
        self.scroll_area_results.setObjectName("scroll_area_results")
        
        self.text_edit_search = SearchBox(self.tab_search)
        self.text_edit_search.setGeometry(QtCore.QRect(150, 0, 600, 30))
        self.text_edit_search.setObjectName("text_edit_search")
        
        self.combo_box_source = QtWidgets.QComboBox(self.tab_search)
        self.combo_box_source.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.combo_box_source.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combo_box_source.setObjectName("combo_box_source")
        self.combo_box_source.addItem("")
        self.label_error = QtWidgets.QLabel(self.tab_search)
        self.label_error.setGeometry(QtCore.QRect(150, 30, 651, 30))
        self.label_error.setText("")
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
        self.combo_box_source.setItemText(0, _translate("ComicDownloaderWindow", "Funbe"))
        
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_search), _translate("ComicDownloaderWindow", "Search"))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_downloads), _translate("ComicDownloaderWindow", "Downloads"))
        self.menu_tools.setTitle(_translate("ComicDownloaderWindow", "Tools"))
        self.action_about.setText(_translate("ComicDownloaderWindow", "About"))
        self.action_log.setText(_translate("ComicDownloaderWindow", "Show Log"))
    
    def btn_push_search_click(self):
        print(self.text_edit_search.toPlainText())

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
        info = QtWidgets.QMessageBox()
        info.setWindowTitle("Info")
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setText("Made by: Anonymous Pomp (anonymouspomp@gmail.com)" + "\n"
                     "https://github.com/AnonymousPomp/Comic-Downloader")
        info.exec_()

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

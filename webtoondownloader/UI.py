from webtoondownloader import IconFromBase64, IMAGES, SearchThread, save_location, where

import webtoonscraper.naver
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from webbrowser import open_new_tab
from threading import Thread
import requests


class UiComicDownloaderWindow(QtWidgets.QMainWindow):
	sig = QtCore.pyqtSignal(int, str)
	search_query = ""

	def __init__(self, *args, **kwargs):
		super(UiComicDownloaderWindow, self).__init__(*args, **kwargs)
		uic.loadUi(where() + "/webtoondownloader.ui", self)
		self.setWindowIcon(IconFromBase64(IMAGES.IMG_LOGO_48))

		self.scrollArea_results = self.findChild(QtWidgets.QScrollArea, "scrollArea_results")
		self.scrollAreaWidgetContents_results = self.findChild(QtWidgets.QWidget, "scrollAreaWidgetContents_results")
		self.v_box_layout_results = self.findChild(QtWidgets.QVBoxLayout, "verticalLayout")
		self.scrollArea_results.setWidget(self.scrollAreaWidgetContents_results)
		self.scrollAreaWidgetContents_results.setLayout(self.v_box_layout_results)

		self.text_edit_search = self.findChild(QtWidgets.QLineEdit, "lineEdit_search")
		self.text_edit_search.setText("신의 탑")  # for testing
		self.text_edit_search.textChanged.connect(self.line_edit_search)
		self.text_edit_search.returnPressed.connect(self.search_webtoon)

		self.label_error = self.findChild(QtWidgets.QLabel, "label_status")

		self.btn_push_search = self.findChild(QtWidgets.QPushButton, "pushButton_search")
		self.btn_push_search.clicked.connect(self.search_webtoon)
		self.btn_push_search.setIcon(IconFromBase64(IMAGES.IMG_SEARCH))

		self.combo_box_source = self.findChild(QtWidgets.QComboBox, "comboBox_source")

		self.scroll_area_downloads = self.findChild(QtWidgets.QWidget, "scrollArea_downloads")

		self.action_about = self.findChild(QtWidgets.QAction, "actionAbout")
		self.action_about.triggered.connect(self.about_click)

		self.search_thread = SearchThread()
		self.search_thread.sig.connect(self.search_thread_catch)
		self.sig.connect(self.search_thread.search_runner)
		self.search_thread.start()

		self.text_edit_search.setFocus()

	def search_webtoon(self):
		query = self.text_edit_search.text().strip()
		if query == "":
			self.label_error.setText("You haven't entered anything to search")
			return
		elif self.search_query == query:
			self.label_error.setText("You're searching for the same webtoon")
			return

		self.search_query = query

		self.label_error.setText("Searching...")
		self.sig.emit(self.combo_box_source.currentIndex(), self.search_query)

	def about_click(self):
		text = \
			"""
<center> <h1> Comic Downloader </h1> </center>
Version: %s<br>
Release date: 2020 February 18<br>
License: Apache-2.0 Anonymous Pomp<br>
Email: anonymouspomp@gmail.com<br>
<br>
Source code available on github:<br>
https://github.com/AnonymousPomp/Comic-Downloader<br>""" % "0.0.1"  # todo: get version

		QtWidgets.QMessageBox.about(self, "About", text)

	def search_thread_catch(self, mode, data):
		if mode == self.search_thread.MODE_UPDATE_UI:
			mode, content = data
			if mode == self.search_thread.UI_LABEL_ERROR:
				self.label_error.setText(content)
			else:
				self.label_error.setText("Something has gone Wrong. Update mode not found")
		elif mode == self.search_thread.MODE_SEARCH_RESULT:
			# clear list
			for i in reversed(range(self.v_box_layout_results.count())):
				self.v_box_layout_results.removeWidget(self.v_box_layout_results.itemAt(i).widget())

			# repopulate list
			for search_result in data:
				adding = ComicGroupBox(search_result)
				adding.setFixedSize(adding.size())
				self.v_box_layout_results.addWidget(adding)

	@staticmethod
	def line_edit_search(*args):
		pass


class ComicGroupBox(QtWidgets.QGroupBox):
	def __init__(self, comic_data):
		# 0: URL
		# 1: title
		# 2: type
		# 3: author
		# 4: genre
		# 5: number of episodes
		# 6: latest update

		# todo: get these (in a separate thread)
		# synopsis
		# thumbnail

		super(ComicGroupBox, self).__init__()
		uic.loadUi(where() + "/ComicGroupBox.ui", self)
		self.comic_data = comic_data
		self.comic_URL = comic_data[0] if comic_data else "https://google.com"

		# Thumbnail
		thumbnail = self.findChild(QtWidgets.QLabel, "thumbnail")

		try:
			thumbnail_URL = "https://shared-comic.pstatic.net/thumb/webtoon/183559/thumbnail/thumbnail_IMAG06_cffe8f9f-1968-4c48-b7d5-7d40d48da340.jpg"
			response = requests.get(thumbnail_URL, stream=True)

			if response.status_code == 200:
				image = QtGui.QImage()
				image.loadFromData(response.content)

				thumbnail.setPixmap(QtGui.QPixmap.fromImage(image))
		except requests.exceptions.ConnectionError:
			pass

		# Title
		title = self.findChild(QtWidgets.QLabel, "title")
		self.fill(title, 1)

		# Authors
		authors = self.findChild(QtWidgets.QLabel, "authors")
		self.fill(authors, 3)

		# Last date of update
		update = self.findChild(QtWidgets.QLabel, "update_date")
		self.fill(update, 6, pre="Latest: ")

		# Number of episodes
		number_of_episodes = self.findChild(QtWidgets.QLabel, "episodes")
		self.fill(number_of_episodes, 5)

		# Synopsis
		synopsis = self.findChild(QtWidgets.QLabel, "synopsis")
		self.fill(synopsis, 4)

		# Browse
		btn_browse = self.findChild(QtWidgets.QPushButton, "browse")
		btn_browse.clicked.connect(lambda: open_new_tab(self.comic_URL))
		btn_browse.setIcon(IconFromBase64(IMAGES.IMG_BROWSE))

		# Download
		btn_download = self.findChild(QtWidgets.QPushButton, "download")
		btn_download.clicked.connect(self.download_comics)
		btn_download.setIcon(IconFromBase64(IMAGES.IMG_DOWNLOAD))

	def download_comics(self):
		process = Thread(target=webtoonscraper.naver.episode(self.comic_URL))
		process.start()
		process.join()

	def fill(self, widget, index, **kwargs):
		pre, post = "", ""
		if "pre" in kwargs:
			pre = kwargs["pre"]
		if "post" in kwargs:
			post = kwargs["post"]

		widget.setText(pre + self.comic_data[index] + post if self.comic_data else widget.text())

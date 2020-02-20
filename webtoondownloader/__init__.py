# -*- coding: utf-8 -*-

# todo: update readme.md
# todo: fix entry_points
# todo: fix error management
# todo: logging
# todo: pip install callable (alias?)
# todo: threading pool (maximum 3 episodes at any given moment)
# todo: show download progress
# todo: close all thread when [X] button is clicked
# todo: add custom save location (edit self)
# todo: parallelize search
# todo: show download progress in UI
# todo: put as many multiprocessing as possible
# todo: show downloaded comics
# todo: disable searching when the program is already searching
# todo: add "read" button to downloaded comics
# todo: show time taken to download
# todo: "START" and "END" keyword
# todo: add update checker


style = ""
save_location = None  # todo: save location

import webtoonscraper
import webtoonscraper.naver

from PyQt5 import QtCore, QtGui
from threading import Thread
import os


class IMAGES:
	IMG_DOWNLOAD = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAA8FBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABmRfStAAAAT3RSTlMAAQQICQoLDBIXHCAhJCcoKiwtLi8xMjM0Njg7PD5DREVOT1ldYmNncHFzd3iChYaIj5SVl5ibnqCipbC1t8PHyM7R1drc4OTo6fX3+fv9YEV6XQAAAOVJREFUGBnVwddWwkAARdETldgbYyzYFbFXxK6IWBCE+/9/IziZSVjIu+7NXxIsXVTr1dNp+hh/k1Ue4Tc5eV8T9BpTSiOkR0Vp1wP5u6scKZPqVldbicSerN0wDAty1vBuZEWAkfOA9ygrAoycCrFguyUrAoycE6zgXk4EGDn5gB/H8iLAyKvN0TYq68AYMwQMGmP2FVsFDmXtkCgo1hyGF8U2cbbkHUFDzjrWhhI1eJW3TMeK0gLOlVgAFpXWhKxSZsmqyy3wpETrrKUuM0DmU30V6cg8q49igDVfelePj8sp/otvn/iK48fNmCQAAAAASUVORK5CYII="
	IMG_SEARCH = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABCFBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzxr8JAAAAV3RSTlMAAQIDBAYHCw4PERMUGBseIyQmKCksLjEzNDU3ODo7PENGR05PUFRXW11kZnBxdXd/gIKDkZ2eoKWor7C0t7m8xcfIyszO0dPV19re4OTm6evt7/H19/ntlmEiAAABOElEQVQYGX3BCSMCURgF0DtTTSghITuh7OtESnYKjWSZ+///ie89NUs1zoFnbP34sl45Wk1iqJlH9tQyGDB6w6ByAmG5b4a10gia5QA3Dd/YD5XXwoiJWKrUodJKwPNEZcfAn9gplTJ6lqjMw7dNJYOuFkURQWcUNfyZoLhHSKxDkYS2SzGHsBLFKrQqRRxhKYojaA7JNvrEKCrQXJJ36EdRh9Ym6aCPSXEB7ZrCRNgIxQm0A4oswgoUa9ByFFWEGK8UKWjGF0UeQTsUj+jaonDH4Vugsowu06Fw8+gpUrmFZ5JaNWsCiM89UDuHb5Ndzt0HPTZ8mxzGhm/SYVDzhYoNn7HxyZ73DcNqUrERYEzv19vu29XelAHAalKxEclqULERyWpQWUEkq0FxgGjWM8kc/hE/rCziF8m9fWG4iWOGAAAAAElFTkSuQmCC"
	IMG_BROWSE = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABt6r1GAAAAJHRSTlMAAgMEBQgJCyMkQElVVleFi4yRlZidnrm8wMHDxcjM3uDk5vvXt23NAAAAp0lEQVQ4y83SuxaCMBAE0CWJKFmUlzzloWb+/xstULEgW4iFU+65zcxZou0JCwdPXBESmRuEXDUdISamTAYp5TLIfwMq3wLVE5Q+UH4DjJGBGQYtAd0DvfYDfQGATvuAaufurVoHqnmt06g1ENTLfnWwAiJm5g7omJkPvpoJkIg7/CnIgNFaa62NFhDNlxFI6fTxXW+w/GFM5i6BSRPtz84HXL6j7XkAv4hAOfO2KdAAAAAASUVORK5CYII="
	IMG_LOGO_48 = b"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"


class IconFromBase64(QtGui.QIcon):
	def __init__(self, logo_base64, *args, **kwargs):
		super(IconFromBase64, self).__init__(*args, **kwargs)
		self.icon_pixmap = QtGui.QPixmap()
		self.icon_pixmap.loadFromData(QtCore.QByteArray.fromBase64(logo_base64))
		self.addPixmap(self.icon_pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)


class SearchThread(QtCore.QThread):
	MODE_UPDATE_UI = 1
	MODE_SEARCH_RESULT = 2

	UI_LABEL_ERROR = 1
	sig = QtCore.pyqtSignal(object, object)

	def __init__(self, *args, **kwargs):
		super(SearchThread, self).__init__(*args, **kwargs)

	def search_runner(self, mode, query):
		# todo: fix freezing problem
		Thread(target=self.search, args=(mode, query)).start()

	def search(self, mode, query):
		# 0: URL
		# 1: title
		# 2: type
		# 3: author
		# 4: genre
		# 5: number of episodes
		# 6: latest update

		# synopsis
		# thumbnail

		# Downloading
		result = None
		if mode == webtoonscraper.COMIC_TYPE.NAVER:
			result = webtoonscraper.naver.search(query)
			if result == -1:
				self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "Cannot connect to naver server. Please check your internet connection"))
				return
			elif result == -2:
				self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "[ERROR] Something has gone wrong. The scraper isn't working (naver.search() returned -2)"))
		if not result:
			self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "No search result"))
			return

		number_of_comics = len(result)
		self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "found %s %s" % (number_of_comics, " comic" if number_of_comics is 1 else " comics")))
		self.sig.emit(self.MODE_SEARCH_RESULT, result)


def where():
	return os.path.dirname(__file__)

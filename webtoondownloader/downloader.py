import webtoondownloader.UI

from PyQt5 import QtWidgets
import sys


def run():
	app = QtWidgets.QApplication([])

	screen_resolution = app.desktop().screenGeometry()
	ComicDownloader = webtoondownloader.UI.UiComicDownloaderWindow()

	# start window from the center of the screen
	ComicDownloader.move(screen_resolution.center() - ComicDownloader.rect().center())
	ComicDownloader.show()
	sys.exit(app.exec_())

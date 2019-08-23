# -*- coding: utf-8 -*-
"""
This script returns a list of URL of comics

how to make it into an exe file:
pyinstaller --onefile --icon=icon.ico search.py --hidden-import=queue

where
	0: https://comic.naver.com/webtoon/weekday.nhn
	1: https://comic.naver.com/genre/bestChallenge.nhn
	2: http://webtoon.daum.net
	3: https://funbe16.com
output
	-1: No search result
	-2: Source not recognized
	-3: Option not recognized

test command:
python search.py --query "나 혼자만" --source 3
search.exe --query "나 혼자만" --source 3
"""

from urllib.parse import urlparse
from bs4 import BeautifulSoup
import traceback
import requests
import msvcrt
import sys

# if the values of the variables are the same at the end of the runtime, then something has gone wrong
COMIC_TYPE_NAVER = 0
COMIC_TYPE_NAVER_BEST_CHALLENGE = 1
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3

comic_query = "you shouldn't be seeing this"
source = -1
final = list()


def search_funbe():
	link = 'https://funbe16.com/bbs/search.php?sfl=wr_subject%7C%7Cwr_content&stx={0}'.format(comic_query)

	toon_html = requests.get(link).text
	toon_soup = BeautifulSoup(toon_html, 'html.parser')

	try:
		search_results = toon_soup.select('#title')
	except AttributeError:
		sys.exit(-1)

	for i in search_results:
		final.append("https://funbe16.com" + i.get('href'))


def search_naver(best_challenge=False):
	link = 'https://comic.naver.com/search.nhn?keyword={0}'.format(comic_query)

	toon_html = requests.get(link).text
	toon_soup = BeautifulSoup(toon_html, 'html.parser')

	try:
		search_result = toon_soup.select('#content > div > ul > li > h5 > a')
	except AttributeError:
		sys.exit(-1)

	for i in search_result:
		url = str(i.get('href'))
		if '://' in url:
			final.append(url)
		else:
			final.append('{uri.netloc}'.format(uri=urlparse(link)) + url)


def search_daum():
	pass


if __name__ == "__main__":
	import getopt

	try:
		options, args = getopt.getopt(sys.argv[1:], 'q:s:', ['query=', 'source='])

	except getopt.GetoptError as err:
		sys.exit(-3)

	for option, argument in options:
		if option == '--query' or option == "-q":
			comic_query = argument

		elif option == '--source' or option == "-s":
			if int(argument) == COMIC_TYPE_NAVER:
				# search_naver()
				pass

			elif int(argument) == COMIC_TYPE_NAVER_BEST_CHALLENGE:
				# search_naver(True)
				pass

			elif int(argument) == COMIC_TYPE_DAUM:
				# search_daum()
				pass

			elif int(argument) == COMIC_TYPE_FUNBE:
				search_funbe()

			else:
				pass

		else:
			pass

	for url in final:
		print(url)

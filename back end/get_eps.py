# -*- coding: utf-8 -*-
"""
This script returns a list of episodes of a given comic

how to make it an executable file:
pyinstaller --onefile --icon=icon.ico get_eps.py --hidden-import=queue

output
	-1: No episode in the given toon
	-2: Source not recognized
	-3: Option not recognized
	-4: given URL is not valid

test command:
python get_eps.py --url "https://funbe16.com/나-혼자만-레벨업" --source 3
get_eps.exe --url "https://funbe16.com/나-혼자만-레벨업" --source 3
"""

from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import sys

COMIC_TYPE_NAVER = 0
COMIC_TYPE_NAVER_BEST_CHALLENGE = 1
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3

# if the values of the variables are the same at the end of the runtime, then something has gone wrong
link = "you shouldn't be seeing this"
source = -1

comic_html = None
comic_soup = None


def get_episodes_from_funbe():
	try:
		for i in comic_soup.select('#fboardlist > table > tr > td.content__title')[::-1]:
			print("https://funbe16.com" + i.get("data-role"))

	except AttributeError as err:  # if there are no results
		print(err)
		sys.exit(-1)


def get_episodes_from_naver():
	# incomplete. doesn't work yet
	try:
		for i in comic_soup.select('#content > table > tbody > tr > td.title > a')[::-1]:
			print('{uri.netloc}'.format(uri=urlparse(link)) + i.get('href'))

	except AttributeError as err:  # if there are no results
		print(err)
		sys.exit(-1)


if __name__ == "__main__":
	import getopt

	# acquire arguments
	try:
		options, args = getopt.getopt(sys.argv[1:], 'u:s:', ['url=', 'source='])

		for option, argument in options:
			if option == '--url' or option == "-u":
				link = str(argument)

			elif option == '--source' or option == "-s":
				source = int(argument)

	except getopt.GetoptError as err:
		print(err)
		sys.exit(-3)

	try:
		comic_html = requests.get(link).text
		comic_soup = BeautifulSoup(comic_html, 'html.parser')

		if source == COMIC_TYPE_FUNBE:
			get_episodes_from_funbe()

	except requests.exceptions.ConnectionError as err:
		print(err)
		sys.exit(-4)

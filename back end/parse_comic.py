# -*- coding: utf-8 -*-
"""
This script returns required information about a given comic

output
	-1: Error while requiring data
	-2: Source not recognized
	-3: Option not recognized
	-4: given URL is not valid

data:
	0: title
	1: synopsis
	2: author
	3: last update
	4: number of episodes
	5: thumbnail image link

test command: python parse_comic.py --url "https://funbe13.com/나-혼자만-레벨업" --source 3
"""

from bs4 import BeautifulSoup
import requests
import sys

COMIC_TYPE_NAVER = 0
COMIC_TYPE_NAVER_BEST_CHALLENGE = 1
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3

link = "you shouldn't be seeing this"
data = []
source = -1

comic_html = None
comic_soup = None


def parse_funbe():
	try:
		# title
		data.append(comic_soup.find("meta", attrs={"property": "og:title"}).get("content"))

		# synopsis
		data.append(comic_soup.find("td", attrs={"class": "bt_over"}).text)

		# author
		data.append(comic_soup.find_all("span", attrs={"class": "bt_data"})[2].text)
		
		# latest update
		data.append(comic_soup.select_one("#fboardlist > table > tr:nth-child(1) > td.episode__index").text.strip())

		# number of episodes
		data.append(comic_soup.find_all("span", attrs={"class": "bt_data"})[3].text[2:-1])
		
		# thumbnail image link
		data.append("https://funbe13.com" + comic_soup.select_one("#containerCol > table.bt_view2 > tbody > tr:nth-child(1) > td > a > img").get("src"))
		
	except AttributeError as err:
		print(err)
		sys.exit(-1)


if __name__ == "__main__":
	import getopt
	# acquire arguments
	try:
		options, args = getopt.getopt(sys.argv[1:], 'u:s:', ['url=', 'source='])

	except getopt.GetoptError as err:
		sys.exit(-3)

	for option, argument in options:
		if option == '--url' or option == "-u":
			link = str(argument)

		elif option == '--source' or option == "-s":
			source = int(argument)

	try:
		comic_html = requests.get(link).text
		comic_soup = BeautifulSoup(comic_html, 'html.parser')

	except requests.exceptions.ConnectionError:
		sys.exit(-1)

	if source == COMIC_TYPE_FUNBE:
		parse_funbe()

	for info in data:
		print(info)

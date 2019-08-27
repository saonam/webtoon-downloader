# -*- coding: utf-8 -*-
"""
This script returns information about a given comic

how to make it an executable file:
pyinstaller --onefile --icon=icon.ico parse_comic.py --hidden-import=queue

data:
    0: title
    1: synopsis
    2: author
    3: last update
    4: number of episodes
    5: thumbnail image link
"""

from urllib.parse import urlparse
from bs4 import BeautifulSoup
import traceback
import requests
import sys

ERR_WHILE_REQUITING_DATA = -1
ERR_SOURCE_NOT_RECOGNIZED = -2
ERR_OPTION_NOT_RECOGNIZED = -3
ERR_INVALID_URL = -4
ERR_NO_EPISODE_IN_COMIC = -5

COMIC_TYPE_NAVER = 0
COMIC_TYPE_NAVER_BEST_CHALLENGE = 1
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3

# if the values of the variables are the same at the end of the runtime, then something has gone wrong
link = "you shouldn't be seeing this"
source = -1

comic_html = None
comic_soup = None
data = []


def get_episodes_from_funbe():
    try:
        for i in comic_soup.select('#fboardlist > table > tr > td.content__title')[::-1]:
            print("https://funbe16.com" + i.get("data-role"))
    
    except AttributeError:
        print("[ERROR] No episodes in comic")
        print(traceback.format_exc())
        sys.exit(ERR_NO_EPISODE_IN_COMIC)


def get_episodes_from_naver():
    # incomplete. doesn't work yet
    try:
        for i in comic_soup.select('#content > table > tbody > tr > td.title > a')[::-1]:
            print('{uri.netloc}'.format(uri=urlparse(link)) + i.get('href'))
    
    except AttributeError:
        print("[ERROR] No episodes in comic")
        print(traceback.format_exc())
        sys.exit(ERR_NO_EPISODE_IN_COMIC)


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
        data.append("https://funbe16.com" + comic_soup.select_one("#containerCol > table.bt_view2 > tbody > tr:nth-child(1) > td > a > img").get("src"))
    
    except AttributeError:
        print("[ERROR] Error while parsing funbe comic")
        print(traceback.format_exc())
        sys.exit(ERR_WHILE_REQUITING_DATA)


def usage():
    """
        A function that prints helpful information about how to use the program
    """
    print()
    print("Help:")
    print()
    print("options:")
    print("\t -u or --url <comic_url>")
    print("\t -s or --source <0:NAVER   1:NAVER_BEST_CHALLENGE   2:DAUM   3:FUNBE>  (only source 3 is available at the moment)")
    print()
    print("How to use:")
    print("\t parse_comic.exe -u <comic_url> -s <source_index>")
    print("Example:")
    print("\t parse_comic.exe --url \"https://funbe16.com/나-혼자만-레벨업\" --source 3")
    print()


if __name__ == "__main__":
    import getopt
    
    try:
        options, args = getopt.getopt(sys.argv[1:], 'tu:s:', ["test", 'url=', 'source='])
    
    except getopt.GetoptError:
        print("[ERROR] Error while parsing arguments")
        print(traceback.format_exc())
        sys.exit(ERR_OPTION_NOT_RECOGNIZED)
    
    for option, argument in options:
        if option == "-t" or option == "--test":
            link = "https://funbe16.com/나-혼자만-레벨업"
            source = COMIC_TYPE_FUNBE
        
        elif option == '--url' or option == "-u":
            link = str(argument)
        
        elif option == '--source' or option == "-s":
            source = int(argument)
        
        else:
            print("Unknown argument given:")
            usage()
    
    try:
        comic_html = requests.get(link).text
        comic_soup = BeautifulSoup(comic_html, 'html.parser')
    
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to server")
        print(traceback.format_exc())
        sys.exit(ERR_WHILE_REQUITING_DATA)
    
    if source == COMIC_TYPE_FUNBE:
        get_episodes_from_funbe()
        parse_funbe()
    
    else:
        print("invalid source index:")
        usage()
    
    for info in data:
        print(info)

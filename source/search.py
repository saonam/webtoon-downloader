# -*- coding: utf-8 -*-
"""
more information cam be found at usage()

how to make it an executable file:
pyinstaller --onefile --icon=icon.ico search.py --hidden-import=queue
"""

from urllib.parse import urlparse, quote, unquote
from bs4 import BeautifulSoup
import traceback
import requests
import getopt
import sys
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

COMIC_TYPE_NAVER = 0
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3
COMIC_TYPE_KAKAO = 4


def search_funbe():
    global final
    global comic_query
    
    link = 'https://funbe17.com/bbs/search.php?stx=' + quote(comic_query.strip())
    
    try:
        comic_html = requests.get(link).text
        comic_soup = BeautifulSoup(comic_html, 'html.parser')

    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to server")
        print(traceback.format_exc())
        sys.exit(ERR_WHILE_REQUITING_DATA)
    
    try:
        comics = ["https://funbe17.com" + i.get('href') for i in comic_soup.select('#title')]
    
    except AttributeError:
        print("[ERROR] No search result")
        print(traceback.format_exc())
        sys.exit(ERR_NO_SEARCH_RESULT)
    
    # ########################### get_eps
    try:
        pat = re.compile(r"총 \d+화")
        
        for i in comics:
            comic_html = requests.get(i)
            comic_soup = BeautifulSoup(comic_html.text, "html.parser")
            
            episodes = ["https://funbe17.com" + n.get("data-role") for n in comic_soup.select('#fboardlist > table > tr > td.content__title')[::-1]]
            
            try:
                # title
                title = comic_soup.find("meta", attrs={"property": "og:title"}).get("content")
                if title == "펀비(Funbe)":
                    return
                
                print(unquote(i))
                
                [print(i) for i in episodes]
                
                print(title)

                # synopsis
                print(comic_soup.find("td", attrs={"class": "bt_over"}).text)

                # author
                author = comic_soup.find("span", attrs={"class": "bt_data"}).text.strip()
                if not pat.match(author):
                    print(author)
                else:
                    print("None")
                
                # latest update
                print(comic_soup.select_one("#fboardlist > table > tr:nth-child(1) > td.episode__index").text.strip())

                # number of episodes
                print(comic_soup.find("span", attrs={"class": "tcnt"}).text.split("|")[1].strip()[2:-2])

                # thumbnail image link
                print("https://funbe17.com" + comic_soup.select_one("#containerCol > table.bt_view2 > tbody > tr:nth-child(1) > td > a > img").get("src"))
                print()
                
            except AttributeError:
                print("[ERROR] Error while parsing funbe comic")
                print(traceback.format_exc())
                sys.exit(ERR_WHILE_REQUITING_DATA)

    except AttributeError:
        print("[ERROR] No episodes in comic")
        print(traceback.format_exc())
        sys.exit(ERR_NO_EPISODE_IN_COMIC)


def search_naver():
    global final
    
    link = 'https://comic.naver.com/search.nhn?keyword={0}'.format(comic_query)
    
    comic_html = requests.get(link).text
    comic_soup = BeautifulSoup(comic_html, 'html.parser')
    
    try:
        search_result = comic_soup.select('#content > div > ul > li > h5 > a')
    except AttributeError:
        print("[ERROR] No search result")
        print(traceback.format_exc())
        sys.exit(ERR_NO_SEARCH_RESULT)
    
    for i in search_result:
        url = str(i.get('href'))
        if '://' in url:
            final.append(url)
        else:
            final.append('{uri.netloc}'.format(uri=urlparse(link)) + url)
    # ################## get_eps
    # incomplete. doesn't work yet
    try:
        for i in comic_soup.select('#content > table > tbody > tr > td.title > a')[::-1]:
            print('{uri.netloc}'.format(uri=urlparse(link)) + i.get('href'))

    except AttributeError:
        print("[ERROR] No episodes in comic")
        print(traceback.format_exc())
        sys.exit(ERR_NO_EPISODE_IN_COMIC)


def search_daum():
    global final


def search_kakao():
    global final


def usage():
    """
        A function that prints helpful information about how to use the program
    """
    print()
    print("########################################################################################")
    print("# Help:                                                                                #")
    print("# search.exe: Returns a list of URL of comics that a user is trying to find,           #")
    print("#              as well as some information about that comic                            #")
    print("#                                                                                      #")
    print("# options:                                                                             #")
    print('#     -q or --query "<search_query>"                                                   #')
    print("#     -s or --source <0:NAVER   1:NAVER_BEST_CHALLENGE   2:DAUM   3:FUNBE>             #")
    print("#                                                                                      #")
    print("# How to use:                                                                          #")
    print("#     search.exe -q <search_query> -s <source_index>                                   #")
    print("# Example:                                                                             #")
    print('#     search.exe --query "나 혼자만" --source 3                                        #')  # It looks off but it will be straightened when its printed
    print("# Output:                                                                              #")
    print("#     1:URL                                                                            #")
    print("#     2:TITLE                                                                          #")
    print("#     3:SYNOPSIS                                                                       #")
    print("#     4:AUTHOR                                                                         #")
    print("#     5:LAST UPDATE                                                                    #")
    print("#     6:NUMBER OF EPISODES                                                             #")
    print("#     7:THUMBNAIL IMAGE LINK                                                           #")
    print("########################################################################################")
    print()


if __name__ == "__main__":
    comic_query = None
    source = -1
    
    if not sys.argv[1:]:
        print("[ERROR] No argument is passed")
        usage()
        sys.exit(ERR_NO_ARGUMENT_PASSED)
    
    try:
        options, args = getopt.getopt(sys.argv[1:], 'thq:s:', ["test", "help", 'query=', 'source='])
    
    except getopt.GetoptError as err:
        print("[ERROR] GetoptError:", err)
        usage()
        sys.exit(ERR_OPTION_NOT_RECOGNIZED)
    
    for option, argument in options:
        if option == "--test" or option == "-t":
            comic_query = "나 혼자만"
            source = COMIC_TYPE_FUNBE
        
        elif option == "--help" or option == "-h":
            usage()
            sys.exit(RETURN_ZERO)
        
        elif option == '--query' or option == "-q":
            comic_query = str(argument).strip()
            if len(comic_query.split(" ")) > 2:
                print("[ERROR] please put no more than 2 space")
                sys.exit(ERR_TOO_MANY_SPACE_IN_QUERY)
        
        elif option == '--source' or option == "-s":
            source = int(argument)
        
        else:
            print("[ERROR] Unknown argument detected:", option)
            usage()
            sys.exit(ERR_OPTION_NOT_RECOGNIZED)

    # check if the machine is connected to internet
    try:
        requests.get("http://216.58.192.142")  # IP address of Google

    except requests.exceptions.ConnectionError:
        print("[ERROR] You are not connected to the internet")
        sys.exit(ERR_NOT_CONNECTED_TO_INTERNET)
    
    if not comic_query:  # if comic_query == None
        print("[ERROR] You didn't pass anything to search")
        sys.exit(ERR_NO_QUERY_GIVEN)
    
    elif source == COMIC_TYPE_NAVER:
        print("Naver support is not ready yet")
        sys.exit(ERR_FEATURE_NOT_READY)
    
    elif source == COMIC_TYPE_DAUM:
        print("Daum support is not ready yet")
        sys.exit(ERR_FEATURE_NOT_READY)
    
    elif source == COMIC_TYPE_KAKAO:
        print("Kakao support is not ready yet")
        sys.exit(ERR_FEATURE_NOT_READY)
    
    elif source == COMIC_TYPE_FUNBE:
        search_funbe()
    
    else:
        print("[ERROR] Unrecognized source")
        usage()
        sys.exit(ERR_SOURCE_NOT_RECOGNIZED)

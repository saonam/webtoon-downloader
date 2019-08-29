# -*- coding: utf-8 -*-
"""
more information cam be found at usage()

how to make it an executable file:
pyinstaller --onefile --icon=icon.ico search.py --hidden-import=queue
"""

from urllib.parse import urlparse
from bs4 import BeautifulSoup
import traceback
import requests
import sys

ERR_NO_SEARCH_RESULT = -1
ERR_SOURCE_NOT_RECOGNIZED = -2
ERR_OPTION_NOT_RECOGNIZED = -3
ERR_TOO_MANY_SPACE_IN_QUERY = -4
ERR_NO_QUERY_GIVEN = -5

COMIC_TYPE_NAVER = 0
COMIC_TYPE_NAVER_BEST_CHALLENGE = 1
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3

# if the values of the variables are the same at the end of the runtime, then something has gone wrong
comic_query = "you shouldn't be seeing this"
source = -1
final = []


def search_funbe():
    link = 'https://funbe16.com/bbs/search.php?sfl=wr_subject%7C%7Cwr_content&stx={0}'.format(comic_query)
    
    toon_html = requests.get(link).text
    toon_soup = BeautifulSoup(toon_html, 'html.parser')
    
    try:
        search_results = toon_soup.select('#title')
    
    except AttributeError:
        print("[ERROR] No search result")
        print(traceback.format_exc())
        sys.exit(ERR_NO_SEARCH_RESULT)
    
    for i in search_results:
        final.append("https://funbe16.com" + i.get('href'))


def search_naver(best_challenge=False):
    link = 'https://comic.naver.com/search.nhn?keyword={0}'.format(comic_query)
    
    toon_html = requests.get(link).text
    toon_soup = BeautifulSoup(toon_html, 'html.parser')
    
    try:
        search_result = toon_soup.select('#content > div > ul > li > h5 > a')
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


def search_daum():
    pass


def search_kakao():
    pass


def usage():
    """
        A function that prints helpful information about how to use the program
    """
    print()
    print("Help:")
    print("search.exe: Returns a list of URL of comics that a user is trying to find")
    print()
    print("options:")
    print("\t -q or --query \"<search_query>\"")
    print("\t -s or --source <0:NAVER   1:NAVER_BEST_CHALLENGE   2:DAUM   3:FUNBE>  (only source 3 is available at the moment)")
    print()
    print("How to use:")
    print("\t search.exe -q <search_query> -s <source_index>")
    print("Example:")
    print("\t search.exe --query \"나 혼자만\" --source 3")
    print()


if __name__ == "__main__":
    import getopt
    
    try:
        options, args = getopt.getopt(sys.argv[1:], 'thq:s:', ["test", "help", 'query=', 'source='])
    
    except getopt.GetoptError as err:
        print("[ERROR] Error while parsing arguments")
        print(traceback.format_exc())
        sys.exit(ERR_OPTION_NOT_RECOGNIZED)
    
    for option, argument in options:
        if option == "-t" or option == "--test":
            print("lol")
            comic_query = "나 혼자만"
            source = COMIC_TYPE_FUNBE
        
        elif option == '--query' or option == "-q":
            comic_query = str(argument).strip()
            if len(comic_query.split(" ")) > 2:
                print("[ERROR] please put no more than 2 space")
                sys.exit(ERR_TOO_MANY_SPACE_IN_QUERY)
        
        elif option == '--source' or option == "-s":
            source = int(argument)
        
        elif option == "--help" or option == "-h":
            usage()
        
        else:
            pass
    
    if comic_query == "you shouldn't be seeing this":
        print("[ERROR] You didn't pass anything to search")
        sys.exit(ERR_NO_QUERY_GIVEN)
    
    if source == COMIC_TYPE_NAVER:
        search_naver()
    
    elif source == COMIC_TYPE_NAVER_BEST_CHALLENGE:
        search_naver(True)
    
    elif source == COMIC_TYPE_DAUM:
        search_daum()
    
    elif source == COMIC_TYPE_FUNBE:
        search_funbe()
    
    else:
        print("[ERROR] Unrecognized source")
        usage()
        sys.exit(ERR_SOURCE_NOT_RECOGNIZED)
    
    if len(final) > 0:
        for url in final:
            print(url)
    else:
        print("try to search with more specific keywords")
        sys.exit(ERR_NO_SEARCH_RESULT)

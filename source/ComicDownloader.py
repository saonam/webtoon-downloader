#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
more information cam be found at usage()

how to make it an executable file:
    pyinstaller --onefile --windowed --icon=./Images/icons8-pluto-dwarf-planet-48.png ComicDownloader.py --hidden-import=queue

# todo: remove sys.exit()
# todo: remove print (replace it with log())
# todo: make log window sizable
# todo: iterators -> generators
# todo: remove unnecessary image loading
"""
__author__ = "Anonymous Pomp <anonymouspomp@gmail.com>"

log_message = ""

import time

time_start = time.time()
from decimal import Decimal


def log(message):
    global log_message
    if type(message) is not str:
        message = str(message)
    log_message += "[" + str(Decimal(time.time() - time_start))[:5] + "s] " + message + "\n"


log("[INFO] Program Launched")

from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from natsort import natsorted
from bs4 import BeautifulSoup
from PIL import Image
import subprocess
import threading
import traceback
import requests
import warnings
import shutil
import glob
import json
import time
import sys
import os

log("[INFO] Loaded libraries")

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
ERR_INVALID_URL = -11
ERR_CANNOT_CONNECT_TO_SERVER = -12
ERR_UNDEFINED = -13
ERR_RSS = -14
ERR_COOKIE = -15
ERR_DOWNLOAD = -16
ERR_NO_EPISODE = -17
ERR_NO_IMAGES = -18
ERR_WHILE_STITCHING_IMAGES = -19
ERR_SOURCE_IS_NOT_A_NUMBER = -20
ERR_SOURCE_NOT_GIVEN = -21

COMIC_TYPE_SPOWIKI = 0
COMIC_TYPE_NAVER = 1
COMIC_TYPE_NAVER_BEST_CHALLENGE = 2
COMIC_TYPE_DAUM = 3
COMIC_TYPE_KAKAO = 4

###############################################################################
# Support
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

warnings.filterwarnings("ignore")  # to suppress selenium phantomjs deprecation warning

# if the program has been compiled
if hasattr(sys, "frozen"):
    """
        big thanks to https://stackoverflow.com/users/2682863/user2682863
        got code form: https://stackoverflow.com/questions/46119901/
    """
    
    
    def override_where():
        return os.path.abspath("cacert.pem")
    
    
    import certifi.core
    
    os.environ["REQUESTS_CA_BUNDLE"] = override_where()
    certifi.core.where = override_where
    
    # delay importing until after where() has been replaced
    import requests.utils
    import requests.adapters
    
    # replace these variables in case these modules were
    # imported before we replaced certifi.core.where
    requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
    requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()


def stitch_image(path, location):
    try:
        images = natsorted(glob.glob(path + '/*.*'))  # get a list of images
        
        XY_value_list = [[Image.open(file).size[0], Image.open(file).size[1]] for file in
                         images]  # get the dimension of all the images
        height = int(sum([y for (x, y) in XY_value_list]))
        
        # prepare a empty canvas (may take a lot of space of the memory)
        try:
            img_final = Image.new('RGB', (max([x for (x, y) in XY_value_list]), height), "white")
        except ValueError:
            print()
            print("[ERROR] The comic has no images to stitch")
            sys.exit(ERR_NO_IMAGES)
        y_offset = 0
        
        # loop all images
        for i in range(len(images)):
            img_final.paste(Image.open(images[i]), (0, y_offset))  # paste image...
            y_offset += XY_value_list[i][1]  # and increase y offset!
        
        img_final.save("%s/%s.png" % (location, path), "PNG", quality=100)
    
    except:
        log("[ERROR] [%s] %s" % (ERR_WHILE_STITCHING_IMAGES, traceback.format_exc()))


def mkdir_smart(name):
    """
        A function that creates a directory if it doesn't exists
    """
    try:
        if not os.path.isdir(str(name)):
            os.makedirs(os.path.join(str(name)))
            return True
    except OSError:
        return False


class SearchThread(QtCore.QThread):
    MODE_UPDATE_UI = 1
    MODE_SEARCH_RESULT = 2

    UI_LABEL_ERROR = 1
    sig = QtCore.pyqtSignal(object, object)
    
    def __init__(self, *args, **kwargs):
        super(SearchThread, self).__init__(*args, **kwargs)
    
    def go_search(self, mode, comic_query):
        threading.Thread(target=self.search, args=(mode, comic_query)).start()
    
    def search(self, mode, comic_query):
        final = []
        
        if mode == COMIC_TYPE_NAVER:
            source = "naver"
        elif mode == COMIC_TYPE_NAVER_BEST_CHALLENGE:
            source = "naver best challenge"
        elif mode == COMIC_TYPE_DAUM:
            source = "daum"
        elif mode == COMIC_TYPE_SPOWIKI:
            source = "spowiki"
        elif mode == COMIC_TYPE_KAKAO:
            source = "kakao"
        else:
            source = "undefined"
        
        log("[INFO] Searching for: \"%s\" on %s" % (comic_query, source))
        
        if mode == COMIC_TYPE_NAVER or mode == COMIC_TYPE_NAVER_BEST_CHALLENGE:
            link = 'https://comic.naver.com/search.nhn?keyword={0}'.format(comic_query)
            
            comic_html = requests.get(link).text
            comic_soup = BeautifulSoup(comic_html, 'html.parser')
            
            try:
                search_result = comic_soup.select('#content > div > ul > li > h5 > a')
            except:
                log("[ERROR] [%s] %s" % (ERR_NO_SEARCH_RESULT, traceback.format_exc()))
                return
            
            for i in search_result:
                url = str(i.get('href'))
                if '://' in url:
                    final.append(url)
                else:
                    pass
                    # final.append('{uri.netloc}'.format(uri=urlparse(link)) + url)
            # ################## get_eps
            # incomplete. doesn't work yet
            try:
                for i in comic_soup.select('#content > table > tbody > tr > td.title > a')[::-1]:
                    pass
                    # print('{uri.netloc}'.format(uri=urlparse(link)) + i.get('href'))
            
            except AttributeError:
                print("[ERROR] No episodes in comic")
                print(traceback.format_exc())
                sys.exit(ERR_NO_EPISODE_IN_COMIC)
        elif mode == COMIC_TYPE_DAUM:
            pass
        elif mode == COMIC_TYPE_SPOWIKI:
            link = "https://tv.spowiki.com/bbs/board.php?bo_table=webtoon&wt_title=" + requests.utils.requote_uri(comic_query.strip())
            
            try:
                comic_html = requests.get(link).text
                comic_soup = BeautifulSoup(comic_html, 'html.parser')
            except requests.exceptions.ConnectionError:
                log("[ERROR] Cannot connect to server\n" + traceback.format_exc())
                return ERR_WHILE_REQUITING_DATA
            
            try:
                comics = [comic.get("href") for comic in comic_soup.find_all("a", attrs={"class", "title"})]
                
            except AttributeError:
                log("[ERROR] No search result")
                log(traceback.format_exc())
                sys.exit(ERR_NO_SEARCH_RESULT)
                
            # ########################### get_eps
            try:
                suffix = " comic"
                number_of_comics = len(comics)
                if number_of_comics > 1:
                    suffix += "s"
                suffix += "..."
                
                for i in range(len(comics)):
                    self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "parsing [%s/%s] %s" % (i, number_of_comics, suffix)))
                    
                    final.append(list())
                    
                    comic_html = requests.get(comics[i])
                    comic_soup = BeautifulSoup(comic_html.text, "html.parser")
                    
                    episodes = [episode.get("href") for episode in comic_soup.select("#fboardlist > div > table.bt-table > tbody > tr > td > a")[::-1]]
                    
                    try:
                        # title
                        title = comic_soup.select_one("#wt_view > div.explain > h2 > a").text
                        
                        final[i].append(episodes)
                        
                        final[i].append(title)
                        
                        # comic URL
                        final[i].append(comics[i])
                        
                        # synopsis
                        final[i].append(comic_soup.select_one("#wt_view > div.overview").text.strip())
                        
                        # author
                        final[i].append(comic_soup.select_one("dl.summ > dd:nth-child(2)").text)
                        
                        # latest update
                        final[i].append(comic_soup.select_one("#fboardlist > div:nth-child(10) > table > tbody > tr:nth-child(1) > td.td_date").text)
                        
                        # number of episodes
                        final[i].append(len(episodes))
                        
                        # thumbnail image link
                        final[i].append(comic_soup.select_one("#wt_view > div.thumb > a > img").get("src"))
                        
                    except AttributeError:
                        print("[ERROR] Error while parsing funbe comic")
                        print(traceback.format_exc())
                        sys.exit(ERR_WHILE_REQUITING_DATA)
                    
            except AttributeError:
                print("[ERROR] No episodes in comic")
                print(traceback.format_exc())
                sys.exit(ERR_NO_EPISODE_IN_COMIC)
        elif mode == COMIC_TYPE_KAKAO:
            pass
        
        if not final:
            self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "No search result"))
            return
        
        suffix = " comic"
        number_of_comics = len(final)
        if number_of_comics > 1:
            suffix += "s"
        
        self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "found %s %s" % (number_of_comics, suffix)))
        
        self.sig.emit(self.MODE_SEARCH_RESULT, final)


###############################################################################
# funbe
def funbe(url, ep_name):
    """
        A function that downloads a episode of comic from https://funbe19.com
    """
    
    def funbe_image(i, image_url):
        img = requests.get(image_url, headers=headers).content  # get image
        open(ep_name + "/" + str(i + 1) + ".jpg", "wb").write(img)  # write image
    
    print("[INFO] Downloading:", url)
    
    try:
        print("[INFO] Loading page (it may take a while)...")
        driver = webdriver.PhantomJS(service_args=['--load-images=no'])
        # driver.get("https://funbe19.com" + requests.utils.requote_uri(urlparse(url).path))
        
        comic_html = driver.page_source
        comic_soup = BeautifulSoup(comic_html, 'html.parser')
    
    except requests.exceptions.ConnectionError:
        print()
        print("[ERROR] Cannot connect to funbe server. Please check your internet connection")
        print(traceback.format_exc())
        sys.exit(ERR_CANNOT_CONNECT_TO_SERVER)
    
    try:
        # acquire list of urls of each image that composes the entire comic
        # usually, to save loading time, a comic is fragmented into smaller pieces
        imgs_links = ["https://funbe19.com" + i.get("src") for i in comic_soup.select("#toon_img > img")]
        # images_length = len(imgs_links)
        
        # actual downloading happens here
        ep_name = comic_soup.select_one("head > title").text.strip()  # get the episode name
        mkdir_smart(ep_name)  # create directory where the comic will be saved if it doesn't exist already
        
        print("[INFO] Downloading images...")
        
        tasks = []
        for i, image in enumerate(imgs_links):
            print("[EP]{0}[I]{1}".format(ep_name, i + 1))
            tasks.append(threading.Thread(target=funbe_image, args=(i, image), name="funbe_image_download_thread_%s" % i))
            tasks[i].start()
        
        [i.join() for i in tasks]
    
    except requests.exceptions.MissingSchema:
        print()
        print("[ERROR] The given URL link is invalid")
        print(traceback.format_exc())
        sys.exit(ERR_INVALID_URL)
    
    try:
        print("[INFO] Stitching image...")
        stitch_image(ep_name, "/..")
        shutil.rmtree(ep_name, ignore_errors=True)
    
    except Exception:
        print()
        print("[ERROR] Error while stitching images")
        print(traceback.format_exc())
        pass


###############################################################################
# Naver
WEEKLY_WEBTOON = 1
CHALLENGE_BEST = 2


def naver_image(outfile, referer, image, cmp_no=False):
    res = requests.get(image, headers={'Referer': referer})
    
    if res.status_code != 200:
        print("[ERROR] response code = %d, content: %s" % (res.status_code, res.content))
        return 1
    
    if cmp_no:
        result_url_no = res.url.split('&')[-1]
        request_url_no = image.split('&')[-1]
        if result_url_no != request_url_no:
            print("[ERROR] different url no. (request_url_no: %s, result_url_no: %s), It may be the LAST episode" % (request_url_no, result_url_no))
            return 1
    
    print("[INFO] downloading: %s" % outfile)
    with open(outfile, "wb") as f:
        f.write(res.content)
    return 0


def naver(title_id, title, episode_start, episode_end, output_dir, best):
    if title is None:
        title = ""
    
    mkdir_smart(output_dir + title)
    
    find_strings = [
        "https://imgcomic.naver.com/webtoon/" + title_id + "/",
        "https://imgcomic.naver.net/webtoon/" + title_id + "/",
        "https://image-comic.pstatic.net/webtoon/" + title_id + "/"]
    
    find_string_for_best_challenge = ["https://imgcomic.naver.net/nas/user_contents_data/challenge_comic", ""]
    
    retry_episode = 0
    comic_type = WEEKLY_WEBTOON
    
    if best:
        comic_type = CHALLENGE_BEST
    
    for episode in range(episode_start, episode_end + 1):
        if os.path.isfile(".\\output.output"):
            os.system("del .\\output.output")
        
        if comic_type == WEEKLY_WEBTOON:
            print("[INFO] Downloading naver web comic...")
            page_url = "https://comic.naver.com/webtoon/detail.nhn?titleId=%s&no=%d" % (title_id, episode)
            referer = "https://comic.naver.com/webtoon/detail.nhn?titleId=%s&no=%d" % (title_id, episode)
        
        else:
            print("[INFO] Downloading naver best challenge...")
            page_url = "https://comic.naver.com/bestChallenge/detail.nhn?titleId=%s&no=%d" % (title_id, episode)
            referer = "https://comic.naver.com/bestChallenge/detail.nhn?titleId=%s&no=%d" % (title_id, episode)
        
        if naver_image("./output.output", referer, page_url, True) != 0:
            if retry_episode < 5:
                retry_episode += 1
                continue
            print("[INFO] Finish!")
            break
        
        retry_episode = 0
        
        output_file = open(".\\output.output", "r")
        
        img_list = []
        seq = 0
        s_idx = -1
        for line in output_file.readlines():
            line = line.strip()
            
            if comic_type == WEEKLY_WEBTOON:
                for find_string in find_strings:
                    s_idx = line.find(find_string)
                    if s_idx != -1:
                        break
            else:
                s_idx = line.find(find_string_for_best_challenge[0])
            
            if s_idx != -1:
                seq += 1
                e_idx = line[s_idx:].find('"')
                image_url = line[s_idx:s_idx + e_idx]
                if image_url[-4:].lower() == ".jpg" or image_url[-4:].lower() == ".png" or image_url[
                                                                                           -4:].lower() == ".gif":
                    output_name = "%s%s/%s_%03d_%03d.jpg" % (output_dir, title, title, episode, seq)
                    
                    result = naver_image(output_name, referer, image_url)
                    if result != 0:
                        print('[ERROR] Failed download')
                    img_list.append(output_name)
        
        output_file.close()


###############################################################################
# Daum
COOKIEURL = "http://cartoon.media.daum.net/webtoon/viewer/"
VIEWER = "http://cartoon.media.daum.net/webtoon/viewer_images.js?webtoon_episode_id="


def parsing_rss(rss):
    idlist = []
    item = False
    
    if os.path.isfile(".\\out.output"):
        os.system("del .\\out.output")
    curl_cmd = "curl -s -o .\\out.output " + rss
    curl = subprocess.Popen(curl_cmd, shell=True)
    for i in range(0, 50):  # 5 seconds
        time.sleep(0.1)
        if curl.poll():
            break
    
    if not os.path.isfile(".\\out.output"):
        print("[ERROR] Failed download RSS file.")
        sys.exit(ERR_RSS)
    
    output_file = open(".\\out.output", "r")
    for line in output_file.readlines():
        line = line.strip()
        
        if line.find("<item>") == 0:
            item = True
        
        if item:
            # Get ID
            if line.find("<link>") == 0:
                idx = line.find("</link>")
                line = line[:idx]
                idx = line.rfind("/")
                if idx < 0:
                    print("[ERROR] Failed parsing RSS file")
                    idlist = []
                    break
                comic_id = line[idx + 1:]
                # push ID to idlist
                idlist.append(comic_id)
            if line.find("</item>") == 0:
                item = False
    output_file.close()
    return idlist


def get_cookie(comic_id):
    cookie = ".\\cookie.jar"
    
    if os.path.isfile(cookie):
        os.system("del " + cookie)
    
    curl_cmd = "curl -s -o ./out.output --cookie-jar " + cookie + " " + COOKIEURL + comic_id
    
    curl = subprocess.Popen(curl_cmd, shell=True)
    
    for i in range(0, 50):  # 5 seconds
        time.sleep(0.1)
        if curl.poll():
            break
    
    if os.path.getsize(cookie) > 0:
        return cookie
    
    print("[ERROR] Failed get cookie")
    sys.exit(ERR_COOKIE)


def get_imginfo(comic_id, cookie):
    if os.path.isfile(".\\out.output"):
        os.system("del .\\out.output")
    
    curl_cmd = "curl -s -o .\\out.output --cookie " + cookie + " " + VIEWER + comic_id
    curl = subprocess.Popen(curl_cmd, shell=True)
    
    for i in range(0, 50):  # 5 seconds
        time.sleep(0.1)
        if curl.poll():
            break
    
    if not os.path.isfile(".\\out.output"):
        print("[ERROR] Failed download page.")
        sys.exit(ERR_CANNOT_CONNECT_TO_SERVER)
    
    output_file = open(".\\out.output", "r")
    comic_dict = json.loads(output_file.read(), encoding="utf8")
    output_file.close()
    
    return comic_dict


def daum(title, episode_start, episode_end, output_dir):
    idlist = parsing_rss("")
    idlist.reverse()
    
    if len(idlist) < 1:
        print("[ERROR] Not found episode in RSS")
        sys.exit(ERR_RSS)
    
    episode = 0
    cookie = None
    
    for comic_id in idlist:
        if cookie is None:
            cookie = get_cookie(comic_id)
        
        episode += 1
        
        if episode_start > episode:
            continue
        
        if episode_end < episode:
            break
        
        info = get_imginfo(comic_id, cookie)
        
        if title is None:
            title = info["title"].encode("euc-kr")
        
        title = title.translate(None, '\\/:*?"<>|').strip()
        if not os.path.isdir(output_dir + title):
            os.makedirs(output_dir + title)
        
        # get episode title
        # episode_title = info["episodeTitle"].encode("euc-kr").translate(None, '\\/:*?"<>|').strip()
        
        # get image
        img_list = []
        # img_output = "%s%s\\%s_%03d_%s.jpg" % (output_dir, title, title, episode, episode_title)
        sequence = 0
        
        for img in info["images"]:
            # flash type should pass.
            if 'mediaType' in img and img["mediaType"] == "flash":
                continue
            
            sequence += 1
            
            output_name = "%s%s\\%s_%03d_%03d.jpg" % (output_dir, title, title, episode, sequence)
            wget_cmd = 'wget -O "' + output_name + '" ' + img["url"]  # output_name.decode("euc-kr")
            
            result = os.system(wget_cmd.encode("euc-kr"))
            if result != 0:
                print("[ERROR] Failed download")
                sys.exit(ERR_CANNOT_CONNECT_TO_SERVER)
            
            img_list.append(output_name)


###############################################################################
class UiComicDownloaderWindow(QtWidgets.QMainWindow):
    sig = QtCore.pyqtSignal(int, str)
    
    def __init__(self, *args, **kwargs):
        super(UiComicDownloaderWindow, self).__init__(*args, **kwargs)
        self.width, self.height = 800, 500
        
        self.setObjectName("ComicDownloaderWindow")
        self.setFixedSize(self.width, self.height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setWindowTitle("Comic Downloader")
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
        self.v_box_layout_results.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.widget_results_scroll.setLayout(self.v_box_layout_results)
        self.scroll_area_results_all = QtWidgets.QVBoxLayout()
        self.scroll_area_results_all.addWidget(self.scroll_area_results)
        self.scroll_area_results.setObjectName("scroll_area_results")
        
        self.text_edit_search = SearchBox(self.tab_search)
        self.text_edit_search.setPlaceholderText("Search")
        self.text_edit_search.setGeometry(QtCore.QRect(150, 0, 600, 30))
        self.text_edit_search.setObjectName("text_edit_search")
        
        self.combo_box_source = QtWidgets.QComboBox(self.tab_search)
        self.combo_box_source.setGeometry(QtCore.QRect(0, 0, 150, 30))
        self.combo_box_source.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combo_box_source.setObjectName("combo_box_source")
        self.label_error = QtWidgets.QLabel(self.tab_search)
        self.label_error.setGeometry(QtCore.QRect(150, 30, 651, 30))
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
        
        self.text_edit_search.setFocus()
        self.text_edit_search.setText("나 혼자만 레벨업")
        
        self.search_thread = SearchThread()
        
        self.search_thread.sig.connect(self.search_thread_catch)
        self.sig.connect(self.search_thread.go_search)
        
        self.search_thread.start()
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.combo_box_source.addItem("Funbe")
        # self.combo_box_source.addItem("Naver")
        # self.combo_box_source.addItem("Daum")
        # self.combo_box_source.addItem("Kakao")
        
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_search), _translate("ComicDownloaderWindow", "Search"))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_downloads), _translate("ComicDownloaderWindow", "Downloads"))
        self.menu_tools.setTitle(_translate("ComicDownloaderWindow", "Tools"))
        self.action_about.setText(_translate("ComicDownloaderWindow", "About"))
        self.action_log.setText(_translate("ComicDownloaderWindow", "Show Log"))
    
    def btn_push_search_click(self):
        self.label_error.setText("Searching...")
        # self.btn_push_search.setEnabled(False)
        
        search_query = self.text_edit_search.text().strip()
        
        if not search_query:
            self.label_error.setText("You haven't entered anything to search")
            return
        
        self.sig.emit(self.combo_box_source.currentIndex(), search_query)
        
    def about_click(self):
        text = "<center>" \
               "<h1>Comic Downloader</h1>" \
               "</center>" \
               "Version: v4-alpha<br>" \
               "Release date: 2019 October 1<br>" \
               "Copyright: CC-BY 4.0 &copy; AnonymousPomp<br>" \
               "Email: anonymouspomp@gmail.com<br>" \
               "<br><br>" \
               "Source code available on github:<br>" \
               "https://github.com/AnonymousPomp/Comic-Downloader<br>"
        QtWidgets.QMessageBox.about(self, "About", text)
    
    def log_click(self):
        log("[INFO] Displaying Log")
        ScrollMessageBox(self).exec_()
        
    def search_thread_catch(self, data1, data2):
        if data1 == self.search_thread.MODE_UPDATE_UI:
            mode, data = data2
            if mode == self.search_thread.UI_LABEL_ERROR:
                self.label_error.setText(data)
            else:
                print("yo wut?")
        elif data1 == self.search_thread.MODE_SEARCH_RESULT:
            for search_result in data2:
                self.v_box_layout_results.addWidget(ComicGroupBox(search_result))


class SearchBox(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            ComicDownloader.btn_push_search_click()
        else:
            super().keyPressEvent(qKeyEvent)


class ScrollMessageBox(QtWidgets.QMessageBox):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMessageBox.__init__(self, *args, **kwargs)
        scroll = QtWidgets.QScrollArea(self)
        scroll.setWidgetResizable(True)
        
        self.content = QtWidgets.QWidget()
        scroll.setWidget(self.content)
        lay = QtWidgets.QVBoxLayout(self.content)
        lab = QtWidgets.QLabel(log_message, self)
        lab.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        lay.addWidget(lab)
        
        self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
        self.setStyleSheet("QScrollArea{min-width:700 px; min-height: 400px}")


class ComicGroupBox(QtWidgets.QGroupBox):
    """
    search_result:
        0 list episodes
        1 str title
        2 str comic URL
        3 str synopsis
        4 str authors
        5 str last date of update
        6 str total episodes
        7 str thumbnail
    """
    def __init__(self, comic_data):
        super(ComicGroupBox, self).__init__()
        self.setFixedSize(760, 160)
        
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        layout_groupbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout_groupbox)
        
        # Thumbnail
        thumbnail = QtWidgets.QLabel(self)
        thumbnail.setFixedSize(200, 150)
        thumbnail.move(10, 10)
        response = requests.get(comic_data[7], stream=True)
        if response.status_code == 200:
            image = QtGui.QImage()
            image.loadFromData(response.content)
            
            # thumbnail.setAlignment(QtCore.Qt.AlignCenter)
            thumbnail.setPixmap(QtGui.QPixmap.fromImage(image))
        
        # Title
        title = QtWidgets.QLabel(comic_data[1], self)
        title.move(300, 0)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    screen_resolution = app.desktop().screenGeometry()
    log("[INFO] Displaying GUI")
    ComicDownloader = UiComicDownloaderWindow()
    ComicDownloader.move(screen_resolution.center() - ComicDownloader.rect().center())
    ComicDownloader.show()
    sys.exit(app.exec_())

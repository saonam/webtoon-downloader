# -*- coding: utf-8 -*-

# todo: fix error management
# todo: remove print (replace it with log())
# todo: make log window sizable
# todo: iterators -> generators
# todo: remove unnecessary image loading
# todo: threading pool (maximum 3 episodes at any given moment)
# todo: update documentation
# todo: show download progress
# todo: close all thread when [X] button is clicked
# todo: yield
# todo: add custom save location
# todo: add nsfw filter
# todo: add watermark remover
# todo: parallelize search
# todo: show download progress in UI
# todo: put as many multiprocessing as possible
# todo: download in "comics/" directory
# todo: show downloaded  comics
# todo: add tutorial mode
# todo: make data_save file (pkl)
# todo: disable searching when the program is already searching
# todo: add "read" button to downloaded comics
# todo: add update checker
# todo: show time taken to download
# todo: check if images_downloaded works

__version__ = "v4-alpha"

log_message = ""

from time import time, sleep

time_start = time()
from decimal import Decimal


def log(message):
    global log_message
    if type(message) is not str:
        message = str(message)
    log_message += "[" + str(Decimal(time() - time_start))[:5] + "s] " + message + "\n"


log("[INFO] Program Launched")

from multiprocessing.dummy import Pool as ThreadPool
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from webbrowser import open_new_tab
from traceback import format_exc
from natsort import natsorted
from bs4 import BeautifulSoup
from threading import Thread
from subprocess import Popen
from shutil import rmtree
from json import loads
from glob import glob
from PIL import Image
import requests
import sys
import os

log("[INFO] Loaded libraries")

COMIC_TYPE_SPOWIKI = 0
COMIC_TYPE_NAVER = 1
COMIC_TYPE_NAVER_BEST_CHALLENGE = 2
COMIC_TYPE_DAUM = 3
COMIC_TYPE_KAKAO = 4

IMG_DOWNLOAD = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAA8FBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABmRfStAAAAT3RSTlMAAQQICQoLDBIXHCAhJCcoKiwtLi8xMjM0Njg7PD5DREVOT1ldYmNncHFzd3iChYaIj5SVl5ibnqCipbC1t8PHyM7R1drc4OTo6fX3+fv9YEV6XQAAAOVJREFUGBnVwddWwkAARdETldgbYyzYFbFXxK6IWBCE+/9/IziZSVjIu+7NXxIsXVTr1dNp+hh/k1Ue4Tc5eV8T9BpTSiOkR0Vp1wP5u6scKZPqVldbicSerN0wDAty1vBuZEWAkfOA9ygrAoycCrFguyUrAoycE6zgXk4EGDn5gB/H8iLAyKvN0TYq68AYMwQMGmP2FVsFDmXtkCgo1hyGF8U2cbbkHUFDzjrWhhI1eJW3TMeK0gLOlVgAFpXWhKxSZsmqyy3wpETrrKUuM0DmU30V6cg8q49igDVfelePj8sp/otvn/iK48fNmCQAAAAASUVORK5CYII="
IMG_SEARCH = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAABCFBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzxr8JAAAAV3RSTlMAAQIDBAYHCw4PERMUGBseIyQmKCksLjEzNDU3ODo7PENGR05PUFRXW11kZnBxdXd/gIKDkZ2eoKWor7C0t7m8xcfIyszO0dPV19re4OTm6evt7/H19/ntlmEiAAABOElEQVQYGX3BCSMCURgF0DtTTSghITuh7OtESnYKjWSZ+///ie89NUs1zoFnbP34sl45Wk1iqJlH9tQyGDB6w6ByAmG5b4a10gia5QA3Dd/YD5XXwoiJWKrUodJKwPNEZcfAn9gplTJ6lqjMw7dNJYOuFkURQWcUNfyZoLhHSKxDkYS2SzGHsBLFKrQqRRxhKYojaA7JNvrEKCrQXJJ36EdRh9Ym6aCPSXEB7ZrCRNgIxQm0A4oswgoUa9ByFFWEGK8UKWjGF0UeQTsUj+jaonDH4Vugsowu06Fw8+gpUrmFZ5JaNWsCiM89UDuHb5Ndzt0HPTZ8mxzGhm/SYVDzhYoNn7HxyZ73DcNqUrERYEzv19vu29XelAHAalKxEclqULERyWpQWUEkq0FxgGjWM8kc/hE/rCziF8m9fWG4iWOGAAAAAElFTkSuQmCC"
IMG_BROWSE = b"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABt6r1GAAAAJHRSTlMAAgMEBQgJCyMkQElVVleFi4yRlZidnrm8wMHDxcjM3uDk5vvXt23NAAAAp0lEQVQ4y83SuxaCMBAE0CWJKFmUlzzloWb+/xstULEgW4iFU+65zcxZou0JCwdPXBESmRuEXDUdISamTAYp5TLIfwMq3wLVE5Q+UH4DjJGBGQYtAd0DvfYDfQGATvuAaufurVoHqnmt06g1ENTLfnWwAiJm5g7omJkPvpoJkIg7/CnIgNFaa62NFhDNlxFI6fTxXW+w/GFM5i6BSRPtz84HXL6j7XkAv4hAOfO2KdAAAAAASUVORK5CYII="
IMG_LOGO_48 = b"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"

###############################################################################
# Support
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

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


def stitch_image(images_path, location):
    try:
        if not os.path.exists(location):
            mkdir_smart(location)
        
        images = natsorted(glob(images_path + '/*.*'))  # get a list of images
        
        XY_value_list = [[Image.open(file).size[0], Image.open(file).size[1]] for file in images]  # get the dimension of all the images
        height = int(sum([y for (x, y) in XY_value_list]))
        
        # prepare a empty canvas (may take a lot of space of the memory)
        try:
            img_final = Image.new('RGB', (max([x for (x, y) in XY_value_list]), height), "white")
        except ValueError:
            print()
            print("[ERROR] The comic has no images to stitch")
            return
        y_offset = 0
        
        # loop all images
        for i in range(len(images)):
            img_final.paste(Image.open(images[i]), (0, y_offset))  # paste image...
            y_offset += XY_value_list[i][1]  # and increase y offset!
        
        img_final.save("%s.png" % images_path, "PNG", quality=100)
        
    except:
        log("[ERROR] Cannot stitch images\n%s" % format_exc())


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


###############################################################################
# Spowiki
def download_spowiki(url):
    """
        A function that downloads a episode of comic from https://tv.spowiki.com/
    """
    
    def spowiki_image(i, image_url):
        try:
            img = requests.get(image_url, headers=headers).content  # get image
            
            if image_url[-3:-1] == "pn":
                open("comics/%s/%s.png" % (ep_name, str(i + 1)), "wb").write(img)  # write image
            else:
                open("comics/%s/%s.jpg" % (ep_name, str(i + 1)), "wb").write(img)  # write image
        
        except requests.exceptions.ConnectionError:
            spowiki_image(i, image_url)
        
    log("[INFO] Downloading: %s" % url)
    
    try:
        ComicDownloader.search_thread_catch(SearchThread.MODE_UPDATE_UI, (SearchThread.UI_LABEL_ERROR, "Loading comic (it may take a while)..."))
        log("[INFO] Loading comic...")
        
        comic_html = requests.get(url, headers=headers).content
        comic_soup = BeautifulSoup(comic_html, 'html.parser')
        
    except requests.exceptions.ConnectionError:
        ComicDownloader.search_thread_catch(SearchThread.MODE_UPDATE_UI, (SearchThread.UI_LABEL_ERROR, "[ERROR] Cannot connect to Spowiki server. Please check your internet connection"))
        log("[ERROR] (while downloading %s) Cannot connect to Spowiki server" % url)
        log(format_exc())
        return
    
    try:
        # acquire list of urls of each image that composes the entire comic
        # usually, to save loading time, a comic is fragmented into smaller pieces
        imgs_links = [i.get("src") for i in comic_soup.select("#bo_v_img > a > img")]
        
        # actual downloading happens here
        ep_name = comic_soup.select_one("#bo_v_title").text.strip()
        mkdir_smart("comics/" + ep_name)  # create directory where the comic will be saved

        ComicDownloader.search_thread_catch(SearchThread.MODE_UPDATE_UI, (SearchThread.UI_LABEL_ERROR, "(%s) Downloading images..." % ep_name))
        log("[INFO] (%s) downloading images..." % ep_name)
        
        tasks = []
        for i, image in enumerate(imgs_links):
            tasks.append(Thread(target=spowiki_image, args=(i, image), name="spowiki_image_download_thread_%s" % i))
            tasks[i].start()
        
        [i.join() for i in tasks]
        ComicDownloader.search_thread_catch(SearchThread.MODE_UPDATE_UI, (SearchThread.UI_LABEL_ERROR, "(%s) Downloading images...COMPLETE" % ep_name))
        log("[INFO] (%s) done downloading images" % ep_name)
        
    except requests.exceptions.MissingSchema:
        print("[ERROR] The given URL link is invalid")
        print(format_exc())
        return
    
    try:
        ComicDownloader.search_thread_catch(SearchThread.MODE_UPDATE_UI, (SearchThread.UI_LABEL_ERROR, "(%s) Stitching image..." % ep_name))
        log("[INFO] (%s) Stitching image..." % ep_name)
        
        stitch_image("comics/" + ep_name, "comics/")
        rmtree("comics/" + ep_name, ignore_errors=True)
        ComicDownloader.search_thread_catch(SearchThread.MODE_UPDATE_UI, (SearchThread.UI_LABEL_ERROR, "(%s) COMPLETE" % ep_name))
        log("[INFO] (%s) done stitching image..." % ep_name)
    except Exception:
        print()
        print("[ERROR] Error while stitching images")
        print(format_exc())
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
    curl = Popen(curl_cmd, shell=True)
    for i in range(0, 50):  # 5 seconds
        sleep(0.1)
        if curl.poll():
            break
    
    if not os.path.isfile(".\\out.output"):
        print("[ERROR] Failed download RSS file.")
        return
    
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
    
    curl = Popen(curl_cmd, shell=True)
    
    for i in range(0, 50):  # 5 seconds
        sleep(0.1)
        if curl.poll():
            break
    
    if os.path.getsize(cookie) > 0:
        return cookie
    
    print("[ERROR] Failed get cookie")
    return


def get_imginfo(comic_id, cookie):
    if os.path.isfile(".\\out.output"):
        os.system("del .\\out.output")
    
    curl_cmd = "curl -s -o .\\out.output --cookie " + cookie + " " + VIEWER + comic_id
    curl = Popen(curl_cmd, shell=True)
    
    for i in range(0, 50):  # 5 seconds
        sleep(0.1)
        if curl.poll():
            break
    
    if not os.path.isfile(".\\out.output"):
        print("[ERROR] Failed download page.")
        return
    
    output_file = open(".\\out.output", "r")
    comic_dict = loads(output_file.read(), encoding="utf8")
    output_file.close()
    
    return comic_dict


def daum(title, episode_start, episode_end, output_dir):
    idlist = parsing_rss("")
    idlist.reverse()
    
    if len(idlist) < 1:
        print("[ERROR] Not found episode in RSS")
        return
    
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
                return
            
            img_list.append(output_name)


###############################################################################
class UiComicDownloaderWindow(QtWidgets.QMainWindow):
    sig = QtCore.pyqtSignal(int, str)
    search_query = ""
    
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
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(IMG_LOGO_48))
        icon = QtGui.QIcon()
        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.text_edit_search.setToolTip("Search")
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
        self.btn_push_search.setToolTip("Search")
        self.btn_push_search.setGeometry(QtCore.QRect(750, 0, 50, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_push_search.sizePolicy().hasHeightForWidth())
        self.btn_push_search.setSizePolicy(sizePolicy)
        self.btn_push_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        pixmap1 = QtGui.QPixmap()
        pixmap1.loadFromData(QtCore.QByteArray.fromBase64(IMG_SEARCH))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(pixmap1, QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        
        self.search_thread = SearchThread()
        
        self.search_thread.sig.connect(self.search_thread_catch)
        self.sig.connect(self.search_thread.go_search)
        
        self.search_thread.start()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.combo_box_source.addItem("Spowiki")
        # self.combo_box_source.addItem("Naver")
        # self.combo_box_source.addItem("Daum")
        # self.combo_box_source.addItem("Kakao")
    
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_search),
                                        _translate("ComicDownloaderWindow", "Search"))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_downloads),
                                        _translate("ComicDownloaderWindow", "Downloads"))
        self.menu_tools.setTitle(_translate("ComicDownloaderWindow", "Tools"))
        self.action_about.setText(_translate("ComicDownloaderWindow", "About"))
        self.action_log.setText(_translate("ComicDownloaderWindow", "Show Log"))
        
    def btn_push_search_click(self):
        # self.btn_push_search.setEnabled(False)
        if self.search_query == self.text_edit_search.text().strip():
            self.label_error.setText("That's the same title")
            return
        
        self.search_query = self.text_edit_search.text().strip()
        
        if not self.search_query:
            self.label_error.setText("You haven't entered anything to search")
            return
        
        self.label_error.setText("Searching...")
        self.sig.emit(self.combo_box_source.currentIndex(), self.search_query)
    
    def about_click(self):
        text = "<center>" \
               "<h1>Comic Downloader</h1>" \
               "</center>" \
               "Version: " + __version__ + "<br>" \
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
            # clear list
            for i in reversed(range(self.v_box_layout_results.count())):
                self.v_box_layout_results.itemAt(i).widget().setParent(None)
            
            # repopulate list
            for search_result in data2:
                self.v_box_layout_results.addWidget(ComicGroupBox(search_result))


class SearchThread(QtCore.QThread):
    MODE_UPDATE_UI = 1
    MODE_SEARCH_RESULT = 2
    
    UI_LABEL_ERROR = 1
    sig = QtCore.pyqtSignal(object, object)
    
    def __init__(self, *args, **kwargs):
        super(SearchThread, self).__init__(*args, **kwargs)
    
    def go_search(self, mode, comic_query):
        Thread(target=self.search, args=(mode, comic_query)).start()
    
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
                log("[ERROR] No search result for %s" % comic_query)
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
                    print(link + i.get('href'))
            
            except AttributeError:
                print("[ERROR] No episodes in comic")
                print(format_exc())
                return
                
        elif mode == COMIC_TYPE_DAUM:
            pass
        elif mode == COMIC_TYPE_SPOWIKI:
            link = "https://tv.spowiki.com/bbs/board.php?bo_table=webtoon&wt_title=" + requests.utils.requote_uri(
                comic_query.strip())
            
            try:
                comic_html = requests.get(link).text
                comic_soup = BeautifulSoup(comic_html, 'html.parser')
            except requests.exceptions.ConnectionError:
                log("[ERROR] Cannot connect to spowiki server")
                self.sig.emit(self.MODE_UPDATE_UI, (self.UI_LABEL_ERROR, "[ERROR] Cannot connect to spowiki server. Check your internet connection"))
                return
            
            try:
                comics = [comic.get("href") for comic in comic_soup.find_all("a", attrs={"class", "title"})]
            
            except AttributeError:
                log("[ERROR] No search result")
                log(format_exc())
                return
            
            # ########################### get_eps
            try:
                suffix = " comic"
                number_of_comics = len(comics)
                if number_of_comics > 1:
                    suffix += "s"
                suffix += "..."
                
                for i in range(len(comics)):
                    self.sig.emit(self.MODE_UPDATE_UI,
                                  (self.UI_LABEL_ERROR, "parsing [%s/%s] %s" % (i, number_of_comics, suffix)))
                    
                    final.append(list())
                    
                    comic_html = requests.get(comics[i])
                    comic_soup = BeautifulSoup(comic_html.text, "html.parser")
                    
                    episodes = [episode.get("href") for episode in
                                comic_soup.select("#fboardlist > div > table.bt-table > tbody > tr > td > a")[::-1]]
                    
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
                        final[i].append(comic_soup.select_one(
                            "#fboardlist > div:nth-child(10) > table > tbody > tr:nth-child(1) > td.td_date").text)
                        
                        # number of episodes
                        final[i].append(len(episodes))
                        
                        # thumbnail image link
                        final[i].append(comic_soup.select_one("#wt_view > div.thumb > a > img").get("src"))
                    
                    except AttributeError:
                        print("[ERROR] Error while parsing Spowiki comic")
                        print(format_exc())
                        return
            
            except AttributeError:
                print("[ERROR] No episodes in comic")
                print(format_exc())
                return
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


class SearchBox(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setToolTip("Search")
        self.setPlaceholderText("Search")
        self.setGeometry(QtCore.QRect(150, 0, 600, 30))
        self.setObjectName("text_edit_search")
    
    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            ComicDownloader.btn_push_search_click()
        else:
            super().keyPressEvent(qKeyEvent)


class ScrollMessageBox(QtWidgets.QMessageBox):
    def __init__(self, *args, **kwargs):
        super(ScrollMessageBox, self).__init__(*args, **kwargs)
        scroll = QtWidgets.QScrollArea(self)
        scroll.setWidgetResizable(True)
        
        self.content = QtWidgets.QWidget()
        scroll.setWidget(self.content)
        lay = QtWidgets.QVBoxLayout(self.content)
        lab = QtWidgets.QLabel(log_message, self)
        lab.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        lab.setOpenExternalLinks(True)
        lab.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
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
        self.EPISODES = comic_data[0]
        self.COMIC = comic_data[2]
        
        self.setFixedSize(760, 170)
        self.setStyleSheet("QGroupBox {border:0 ; background-color:lightgray}")
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        layout_groupbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout_groupbox)
        
        # Thumbnail
        thumbnail = QtWidgets.QLabel(self)
        thumbnail.setScaledContents(True)
        thumbnail.setFixedSize(200, 150)
        thumbnail.setAlignment(QtCore.Qt.AlignVCenter)
        thumbnail.move(10, 10)
        
        response = requests.get(comic_data[7], stream=True)
        if response.status_code == 200:
            image = QtGui.QImage()
            image.loadFromData(response.content)
            
            thumbnail.setPixmap(QtGui.QPixmap.fromImage(image))
        
        # Title
        title = QtWidgets.QLabel(comic_data[1], self)
        title.setFixedSize(410, 30)
        title.setStyleSheet("QLabel { font: 20pt}")
        title.move(220, 10)
        
        # Authors
        authors = QtWidgets.QLabel(comic_data[4], self)
        authors.setFixedSize(200, 30)
        authors.setStyleSheet("QLabel { font: 15pt}")
        authors.move(220, 41)
        
        # Last date of update
        update = QtWidgets.QLabel("Latest: " + comic_data[5], self)
        update.setAlignment(QtCore.Qt.AlignRight)
        update.setFixedSize(200, 30)
        update.setStyleSheet("QLabel { font: 15pt}")
        update.move(550, 41)
        
        # Number of episodes
        number_of_episodes = QtWidgets.QLabel("%s episodes" % comic_data[6], self)
        number_of_episodes.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        number_of_episodes.setFixedSize(110, 30)
        number_of_episodes.setStyleSheet("QLabel { font: 12pt}")
        number_of_episodes.move(640, 10)
        
        # Synopsis
        synopsis = QtWidgets.QTextEdit(comic_data[3], self)
        synopsis.setReadOnly(True)
        synopsis.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        synopsis.setFixedSize(450, 75)
        synopsis.setStyleSheet("border:0 ; background-color:lightgray")
        synopsis.move(220, 90)
        
        # Browse
        btn_browse = QtWidgets.QPushButton(self)
        btn_browse.setToolTip("View on browser")
        btn_browse.clicked.connect(lambda: open_new_tab(self.COMIC))
        btn_browse.setFixedSize(40, 40)
        btn_browse_pixmap = QtGui.QPixmap()
        btn_browse_pixmap.loadFromData(QtCore.QByteArray.fromBase64(IMG_BROWSE))
        btn_browse.setIconSize(QtCore.QSize(32, 32))
        btn_browse.setIcon(QtGui.QIcon(btn_browse_pixmap))
        btn_browse.move(710, 90)
        
        # Download
        btn_download = QtWidgets.QPushButton(self)
        btn_download.setToolTip('Download comic')
        btn_download.clicked.connect(self.download)
        btn_download.setFixedSize(40, 40)
        btn_download_pixmap = QtGui.QPixmap()
        btn_download_pixmap.loadFromData(QtCore.QByteArray.fromBase64(IMG_DOWNLOAD))
        btn_download.setIconSize(QtCore.QSize(32, 32))
        btn_download.setIcon(QtGui.QIcon(btn_download_pixmap))
        btn_download.move(710, 130)
        
    def download(self):
        def start_pool():
            pool = ThreadPool(3)
            
            pool.map(download_spowiki, self.EPISODES)
            
            pool.close()
            pool.join()
        
        Thread(target=start_pool).start()
        

class IconFromBase64(QtGui.QIcon):
    def __init__(self, logo_base64, *args, **kwargs):
        super(IconFromBase64, self).__init__(*args, **kwargs)
        self.icon_pixmap = QtGui.QPixmap()
        self.icon_pixmap.loadFromData(QtCore.QByteArray.fromBase64(logo_base64))
        self.addPixmap(self.icon_pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    
    screen_resolution = app.desktop().screenGeometry()
    log("[INFO] Displaying GUI")
    ComicDownloader = UiComicDownloaderWindow()
    ComicDownloader.move(screen_resolution.center() - ComicDownloader.rect().center())
    ComicDownloader.show()
    sys.exit(app.exec_())

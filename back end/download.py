# -*- coding: utf-8 -*-
"""
This script downloads web comic from a source

how to make it an executable file:
pyinstaller --onefile --icon=icon.ico download.py --hidden-import=queue

output
    -1: Invalid URL error
    -2: Source not recognized
    -3: Option not recognized
    -4: Cannot connect to server
    -5: Failed to create save directory
    -6: Invalid episode range
    -7: RSS error
    -8: Failed to get cookie
    -9: Error while requiring episode url
    -10: no episode or the comic doesn't exist

test command:
python download.py --url "https://funbe16.com/나-혼자만-레벨업" --source 3 --episode 1-1
download.exe --url "https://funbe16.com/나-혼자만-레벨업" --source 3 --episode 1-1

python download.py --url "https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon" --source 0 --episode 1-1
download.exe --url "https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon" --source 0 --episode 1-1
"""

from bs4 import BeautifulSoup
from urllib.parse import quote
import subprocess
import traceback
import requests
import shutil
import getopt
import time
import json
import sys
import re
import os


###############################################################################
# Support
COMPILED = False
COMIC_TYPE_NAVER = 0
COMIC_TYPE_NAVER_BEST_CHALLENGE = 1
COMIC_TYPE_DAUM = 2
COMIC_TYPE_FUNBE = 3
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}


def override_where():
    """ overrides certifi.core.where to return actual location of cacert.pem"""
    # change this to match the location of cacert.pem
    return os.path.abspath("cacert.pem")


# is the program compiled?
if hasattr(sys, "frozen"):
    """
        Checks if the code has been compiled
        
        big thanks to https://stackoverflow.com/users/2682863/user2682863
        got code form: https://stackoverflow.com/questions/46119901/
    """
    COMPILED = True
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


def is_connected():
    """
        Check if the machine is connected to the internet.
        It works as long as google isn't blocked.
        Because of this, in countries such as China, the method will return False.

        Despite the disadvantage, I used the script because of simplicity.
        Plus, the comic is in Korean anyway.
    """
    try:
        requests.get("http://216.58.192.142")  # IP address of Google
        return True
    
    except requests.exceptions.ConnectionError:
        return False


def auto_complete_URL(incompleteURL):
    """
        A function that adds "https://" if it doesn't start with it
    """
    if str(incompleteURL).startswith("https://"):
        return incompleteURL
    else:
        return "https://" + incompleteURL


def usage():
    """
        A function that prints helpful information about how to use the program
    """
    print()
    print("Help:")
    print()
    print("options:")
    print("\t --help						   (Shows helpful information)")
    print("\t --url")
    print("\t --episode <episode range>       (default: 1-1)")
    print("\t --location <output directory>   (default: .\\)")
    print("\t --source <daum or naver>        (default: naver)")
    print("\t --merge                         (merge)")
    print("\t --png                           (Save as PNG. (only available with '-m')")
    print()
    print()
    print("sample:")
    print("		downloader.exe --url <link> --episode 1-1")
    print()


###############################################################################
# funbe
def down_funbe(url, location):
    try:
        from selenium import webdriver
        driver = webdriver.PhantomJS()
        driver.get(url)
        
        comic_html = driver.page_source
        comic_soup = BeautifulSoup(comic_html, 'html.parser')
    
    except requests.exceptions.ConnectionError as err:
        print("[ERROR] Cannot connect to funbe server please check your internet connection\n\n", err.with_traceback(sys.exc_info()[2]))
        sys.exit(-4)
    
    try:
        # acquire list of urls of each image that composes the entire comic
        # usually, to save loading time, a comic is fragmented into smaller pieces
        imgs_links = ["https://funbe16.com" + i.get("src") for i in comic_soup.select("#toon_img > img")]
        
        # actual downloading happens here
        ep_name = comic_soup.select_one("#thema_wrapper > div > div > div > div.view-wrap > h1").text.strip()  # get the episode name
        mkdir_smart(location + ep_name)  # create directory where the comic will be saved if it doesn't exists
        
        for i in range(len(imgs_links)):  # for all the images in the comic
            print("[INFO] downloading image #" + str(i + 1) + "/" + str(len(imgs_links)))  # image count (start from 1)
            
            img = requests.get(imgs_links[i]).content  # get image
            open(location + ep_name + "/" + str(i + 1) + ".jpg", "wb").write(img)  # write image
    
    except requests.exceptions.MissingSchema as err:
        print("[ERROR] The given URL link is invalid:", err.with_traceback(sys.exc_info()[2]))
        sys.exit(-1)
    
    try:
        if COMPILED:
            FNULL = open(os.devnull, 'w')
            args = 'merge_image.exe -d "%s"' % (location + ep_name)
            subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)
        else:
            import merge_image
            merge_image.merge_image(location + ep_name)
    except Exception:
        pass


def funbe_main(url, location, episode_start, episode_end):
    """
        A function that downloads comic from https://funbe16.com
    """
    try:
        comic_html = requests.get(url, headers=headers).text
        comic_soup = BeautifulSoup(comic_html, "html.parser")
    
    except requests.exceptions.ConnectionError as err:
        print("[ERROR] Cannot connect to funbe server please check your internet connection\n\n", err.with_traceback(sys.exc_info()[2]))
        sys.exit(-4)
    
    try:
        links = ["https://funbe16.com" + quote(i.get("data-role")) for i in comic_soup.select("#fboardlist > table > tr > td.content__title")][::-1]  # [::-1] flips the list so it starts from episode 1
        
        if episode_start == episode_end and len(links) != 0:
            down_funbe(links[episode_end], location)
        
        elif len(links) == 0:
            print("[ERROR] there are no episodes in the given comic or the comic doesn't exist")
            sys.exit(-10)
        
        else:
            for i in range(episode_start, episode_end + 1):
                down_funbe(links[i], location)
    
    except Exception as err:
        print(traceback.format_exc())
        sys.exit(-9)


###############################################################################
# Naver
WEEKLY_WEBTOON = 1
CHALLENGE_BEST = 2


def down_naver(outfile, referer, url, cmp_no=False):
    res = requests.get(url, headers={'Referer': referer})
    
    if res.status_code != 200:
        print("[ERROR] response code = %d, content: %s" % (res.status_code, res.content))
        return 1
    
    if cmp_no:
        result_url_no = res.url.split('&')[-1]
        request_url_no = url.split('&')[-1]
        if result_url_no != request_url_no:
            print("[ERROR] different url no. (request_url_no: %s, result_url_no: %s), It may be the LAST episode" % (request_url_no, result_url_no))
            return 1
    
    print("[INFO] downloading: %s" % outfile)
    with open(outfile, "wb") as f:
        f.write(res.content)
    return 0


def naver_main(title_id, title, episode_start, episode_end, output_dir, best):
    if title_id == "":
        usage()
    
    if title is None:
        title = ""
    
    if episode_start > episode_end:
        print("[ERROR] Incorrect episode range")
        sys.exit(-6)
    
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
        
        if down_naver("./output.output", referer, page_url, True) != 0:
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
                url = line[s_idx:s_idx + e_idx]
                if url[-4:].lower() == ".jpg" or url[-4:].lower() == ".png" or url[-4:].lower() == ".gif":
                    output_name = "%s%s/%s_%03d_%03d.jpg" % (output_dir, title, title, episode, seq)
                    
                    result = down_naver(output_name, referer, url)
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
        sys.exit(-7)
    
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
    
    # print 'CMD:', curl_cmd
    curl = subprocess.Popen(curl_cmd, shell=True)
    
    for i in range(0, 50):  # 5 seconds
        time.sleep(0.1)
        if curl.poll():
            break
    
    if os.path.getsize(cookie) > 0:
        return cookie
    
    print("[ERROR] Failed get cookie")
    sys.exit(-8)


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
        sys.exit(-4)
    
    output_file = open(".\\out.output", "r")
    comic_dict = json.loads(output_file.read(), encoding="utf8")
    output_file.close()
    
    return comic_dict


def daum_main(rss, title, episode_start, episode_end, output_dir):
    idlist = parsing_rss(rss)
    idlist.reverse()
    
    if len(idlist) < 1:
        print("[ERROR] Not found episode in RSS")
        sys.exit(-7)
    
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
        episode_title = info["episodeTitle"].encode("euc-kr")
        episode_title = episode_title.translate(None, '\\/:*?"<>|').strip()
        
        # get image
        img_list = []
        img_output = "%s%s\\%s_%03d_%s.jpg" % (output_dir, title, title, episode, episode_title)
        sequence = 0
        
        for img in info["images"]:
            # flash type should pass.
            if 'mediaType' in img and img["mediaType"] == "flash":
                continue
            
            sequence += 1
            
            output_name = "%s%s\\%s_%03d_%03d.jpg" % (output_dir, title, title, episode, sequence)
            wget_cmd = 'wget -O "' + output_name + '" ' + img["url"]  # output_name.decode("euc-kr")
            # print 'CMD:', wget_cmd
            result = os.system(wget_cmd.encode("euc-kr"))
            if result != 0:
                print("[ERROR] Failed download")
                sys.exit(-4)
            
            img_list.append(output_name)


###############################################################################
# Main

url = None
location = r".\\"
rss = None
episode_start = 1
episode_end = 1
source = None

try:
    options, arguments = getopt.getopt(sys.argv[1:], "hmu:l:e:r:s:", ["help", "merge", "url=", "location=", "episode=", "rss=", "source="])
    
    for option, argument in options:
        if option == "--help" or option == "-h":
            usage()
        
        elif option == "--merge" or option == "-m":
            merge = True
        
        elif option == "--url" or option == "-u":
            url = str(argument)
        
        elif option == "--location" or option == "-l":
            location = str(argument)
            
            if location[-1] != r"\\" or location[-1] != "/":
                location += r"\\"
        
        elif option == "--episode" or option == "-e":
            try:
                if "-" in argument:
                    parse = argument.split("-")
                    episode_start = int(parse[0])
                    episode_end = int(parse[1])
                else:
                    episode_start = int(argument)
                    episode_end = int(argument)
            
            except Exception as err:
                print("[ERROR] Incorrect episode range")
                print(traceback.format_exc())
                usage()
        
        elif option == "--rss" or option == "-r":
            rss = str(argument)
        
        elif option == "--source" or option == "-s":
            source = int(argument)
        
        else:
            print("[ERROR] Unknown argument detected:", option)
            sys.exit(-3)

except getopt.GetoptError as err:
    print("[ERROR] GetoptError:", err.with_traceback(sys.exc_info()[2]))
    sys.exit(-3)

if source == COMIC_TYPE_NAVER:
    # naver_main(title_id, title, episode_start, episode_end, location, False)
    pass

elif source == COMIC_TYPE_NAVER_BEST_CHALLENGE:
    # naver_main(title_id, title, episode_start, episode_end, location, True)
    pass

elif source == COMIC_TYPE_DAUM:
    # daum_main(rss, title, episode_start, episode_end, location)
    pass

elif source == COMIC_TYPE_FUNBE:
    funbe_main(url, location, episode_start, episode_end)
    pass

else:
    print("[ERROR] Unknown comic source: " + source)
    usage()
    sys.exit(-2)

print("[INFO] download complete")
input("Press Enter to exit")

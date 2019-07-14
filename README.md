# Comic Downloader

>Go to [Download Page (다운로드 페이지)](https://github.com/AnonymousPomp/Comic-Downloader/releases/)

For Korean people, we have prepared a [Korean version of the documentation (한국어 버전의 도큐멘테이션)](https://github.com/AnonymousPomp/Comic-Downloader/blob/master/README_KOR.md) too.

This is a python + C# project that downloads web comic (webtoon) from various sources.*\
*see [Future](#Future) for more information

# [Attention](#attention)
>**I AM NOT RESPONSIBLE FOR WHAT YOU DO WITH MY PROGRAM**

>Downloading comic for commercial use:\
```Downloading web comic for commercial purpose is ILLEGAL. Downloaded comic ONLY for personal use only.```

>The Comic is not English:\
```Note that all the comics are in Korean. So if you are looking for an English comic downloader, this is not what you are looking for.```

>If you have something to say to the developer:\
If you  have any **errors**, **stuck** at any point for whatever reason, or have a **suggestion**, please be kind enough to tell me by writing it at the [issue page](https://github.com/AnonymousPomp/Comic-Downloader/issues), or emailing me at <anonymouspomp@gmail.com>. As a developer, this kind of feedback really helps me, and I will really appreciate each one of it. Thank You :)

>if the downloader doesn't work:\
If you are living in south Korea, you may have to use a proxy or a VPN.
I recommend using [GoodbyeDPI](https://github.com/Include-sys/GUI-for-GoodbyeDPI/releases) program.\
<br>
Plus, there are some other cases such as domain name changes of the comic source. In that case, Try to download the [earliest version](https://github.com/AnonymousPomp/Comic-Downloader/releases/latest) of the program, and tell me your issue at the [issue page](https://github.com/AnonymousPomp/Comic-Downloader/issues), or email me at <anonymouspomp@gmail.com>.

# [Future](#Future)
>Currently, the script only downloads from [funbe](https://funbe13.com/) only. These will be added in the future: [Kakao webtoon](https://page.kakao.com), [Naver webtoon](https://comic.naver.com), [Naver Best Challenge](https://comic.naver.com/genre/bestChallenge.nhn), and [Daum webtoon](http://webtoon.daum.net/).

> A more detailed explanation of how the program works will be added to the documentation


# [developers](#dev)
>All the information listed from now on are for developers who want to learn more about my program

# [How it works](#how)
The project is divided into two large components: the **front end** and the **back end**
- [Front end](https://github.com/AnonymousPomp/Comic-Downloader/tree/master/front%20end)
    - The front end is where the user interacts with the program with GUI.\
    Once the user passes the information needed to download the comic, it will be passed to the back end
- [back end](https://github.com/AnonymousPomp/Comic-Downloader/tree/master/back%20end)
    - The back end is where the magic happens. The  downloading, searching, stitching of images, etc.
# Comic Downloader

>Go to [Download Page](https://github.com/AnonymousPomp/Comic-Downloader/releases/)

This is a python + C# project that downloads web comic (webtoon) from various sources.

Disclaimer: The project is still in development, so don't expect much from it. But please be kind enough to tell me the problems or suggestions so I can add/fix it. :)

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


# [for developers](#dev)
>This is a overview of how the project works as a whole. A more detailed information is commented in the source code.

There are 5 programs in the back end:

1.) search.exe:
- search for a comic with given title.

2.) parse.exe
- returns information about the comic such as the author of the comic, how many episodes there are, the title of the comic, etc.

3.) get_eps.exe
- gets all the episodes in a given comic.

4.) download.exe
- this is where the actual downloading happens.

By executing these programs from the C# front end, users can download a web comic with a simple GUI.

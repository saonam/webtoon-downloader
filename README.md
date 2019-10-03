>Read Documentation in [Korean](https://github.com/AnonymousPomp/Comic-Downloader/blob/master/README_KR.md) ([한국어](https://github.com/AnonymousPomp/Comic-Downloader/blob/master/README_KR.md)로 도큐멘테이션 읽기)

# Comic Downloader

> ## [Download Page](https://github.com/AnonymousPomp/Comic-Downloader/releases/)

This is a program that downloads Korean webcomics from various sources.

The program is still in alpha version (in development), so some part of the program may not be working properly.

downloading takes from 10 second up to 100 second or more per episode depending on your internet connection and the length of the comic.

# Installation
## Windows
You can go to [Download Page](https://github.com/AnonymousPomp/Comic-Downloader/releases/) and download the latest version by clicking on "Assets" and downlaoding the zip file that contains all the data.

## Linux
1.) Clone the repository `git clone https://github.com/AnonymousPomp/Comic-Downloader.git`<br>
2.) Navigate to where the source code is located `cd Comic-Downloader/source`<br>
3.) compile the program by running `pyinstaller --onefile --windowed --icon=icons8-pluto-dwarf-planet-48.png ComicDownloader.py --hidden-import=queue`
or you can execute the script directly by typing `python ComicDownloader.py` (recommended). If you're running the script directly, you may delete all other files including images.

# Warning
>**I have no responsibility over what you do with my program**

>Downloading web comic for commercial use is illegal, and punishable by law. Please download the comics **for personal use ONLY**.

>If there is an **Error** in the program, **stuck** at any point for whatever reason, have a **suggestion** for the project, please be kind enough to tell it to me in the [Issue page](https://github.com/AnonymousPomp/Comic-Downloader/issues), or emailing me at <anonymouspomp@gmail.com>. As a developer, this kind of feedbacks help me a lot, and each and every single one makes my day a bit better. : )

>If the programfails to downlaod the comics, please try using the newest version of the downloader, and if the download still doesn't work, please notify me using methods listed above.

>Some of the comics includes PG16+ contents (including PG19).

>All comics include watermarks. A watermark remover will be added in the near future

# For Developers
>All information from this point on are for developers who want to build upon my program. Ordinary users don't necessarily have to read it.

>This documentation assumes taht you have the following knowledge:
>- Intermediate knowledge about python
>- Basic knowledge about terminal (bash, shell, cmd, etc.)
>- Basic knowledge about VCS(version control system) (git)

>This Project is protected by [CC BY License 4.0](https://creativecommons.org/licenses/by/4.0/)
>
>You are allowed to distribute, remix, tweak, and build up on the project, even commercially, as long as you put a credit for the original creation.
You can find more information [Here](https://en.wikipedia.org/wiki/Creative_Commons_license#Types_of_licenses)

Development Environment:
- Programming Language: [Python 3.6.9](https://www.python.org)
- Designer: [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- IDE: [Pycharm](https://www.jetbrains.com/pycharm/download)

Test environment:
- [Windows 10](https://www.microsoft.com/en-us/software-download/windows10ISO)
- [Linux (Ubuntu 18.04.3 LTS)](https://ubuntu.com/download/desktop)
# Comic Downloader
This is a program that downloads **Korean** web comics from various sources.

The program is still in development phase, so some part of the program may not be working properly, and features might be added and removed very rapidly.

downloading takes from 10 second up to 100 second or more per episode depending on your internet connection and the length of the comic.

>This documentation assumes that you have the following knowledge:
>- Basic knowledge of python
>- Basic knowledge of terminal (bash, shell, cmd, etc.)
>- Basic knowledge of VCS(version control system) (git)

>To understand the code you need to have the following knowledge:
>- Web scraping
>- PyQT
>- multiprocessing

# Installation
> This project requires python 3

There are two ways to run the program. You can either compile the code into and executable file, or just run the code directly.<br>
The only difference is that compiled program takes up more space and requires `cacert.pem` file to run.<br>
Compiled script usually takes up 370MB or more of the storage depending on the libraries installed.<br>
This is the reason why I decided not to upload the executable file. It's faster to compile the script than to download the executable file.


### how to compile
1.) Clone the repository `git clone https://github.com/AnonymousPomp/Comic-Downloader.git`<br>
2.) Navigate to where the source code is located `cd Comic-Downloader`<br>
3.) Install python compiler if you don't have it `pip install PyInstaller`<br>
3.) run `pyinstaller --onefile --windowed --icon=icon.png ComicDownloader.py --hidden-import=queue`. If you're on windows, you can just run `make.bat`<br>
4.) once compiled, all files except the executable and cacert.pem can be deleted.<br>

### Running directly (recommended)
The advantage of running it directly are:
- takes up lesser space
- doesn't require cacert.pem to execute
- easy to fix the errors<br>
- all you need is `ComicDownloader.py`<br>

1.) Install libraries<br>
2.) run `python ComicDownloader.py` to execute<br>
3.) you may delete all the files except `ComicDownloader.py`<br>


# Warning
>This Project is protected by [Apache License 2.0](http://www.apache.org/licenses/)

>**I have no responsibility over what you do with my program**

>Downloading web comic for commercial use is illegal, and punishable by law. Please download the comics **for personal use ONLY**.

>If you have an **Error** in the program, **difficulties** at any point for whatever reason, or a **suggestion** for the project, please be kind enough to tell it to me in the [Issue page](https://github.com/AnonymousPomp/Comic-Downloader/issues), or email me at <anonymouspomp@gmail.com>. As a developer, this kind of feedbacks help me a lot, and each and every single one makes my day a bit better. : )

>If the program fails to download the comics, please try using the newest version of the downloader, and if the download still doesn't work, please notify me using methods listed above.

# More information
Development Environment:
- Programming Language: [Python 3.7.3](https://www.python.org)
- Designer: [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- IDE: [Pycharm Community edition](https://www.jetbrains.com/pycharm/download)
- OS: [Windows 10 Home](https://www.microsoft.com/en-us/software-download/windows10ISO)

Tested on [Windows 10 Home](https://www.microsoft.com/en-us/software-download/windows10ISO) and [Linux (Ubuntu 18.04.3 LTS)](https://ubuntu.com/download/desktop)

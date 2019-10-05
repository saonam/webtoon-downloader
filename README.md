# Comic Downloader
This is a program that downloads Korean webcomics from various sources.

The program is still in alpha version (in development), so some part of the program may not be working properly, and features might be added and removed very rapidly.

downloading takes from 10 second up to 100 second or more per episode depending on your internet connection and the length of the comic.

>This documentation assumes taht you have the following knowledge:
>- Basic knowledge of python
>- Basic knowledge of terminal (bash, shell, cmd, etc.)
>- Basic knowledge of VCS(version control system) (git)

# Installation
> This project requires python 3 installed

There are two ways to run the program. You can either compile the code into and executable file, or just run the code directly. The only difference is that compiled program takes up more space, and that it requires `cecert.pem` file to run. Compiled script usually takes up 370MB or more of the storage depending on the libraries installed. This is the reason why I decided not to upload the executable file. Its faster to compile it than to download it.


### Compile
1.) Clone the repository `git clone https://github.com/AnonymousPomp/Comic-Downloader.git`<br>
2.) Navigate to where the source code is located `cd Comic-Downloader`<br>
3.) Install python compiler `pip install PyInstaller`<br>
3.) compile `pyinstaller --onefile --windowed --icon=icon.png ComicDownloader.py --hidden-import=queue`<br>
4.) once compiled, icon.png can be deleted but you should keep cecert.pem.<br>

### Running directly (recommended)
1.) `python ComicDownloader.py`<br>
2.) If you're running the script directly, you may delete all other files including icon.png and cecert.pem<br>


# Warning
>This Project is protected by [CC BY License 4.0](https://creativecommons.org/licenses/by/4.0/)
>
>You are allowed to distribute, remix, tweak, and build up on the project, even commercially, as long as you put a credit for the original creation.
You can find more information [Here](https://en.wikipedia.org/wiki/Creative_Commons_license#Types_of_licenses)

>**I have no responsibility over what you do with my program**

>Downloading web comic for commercial use is illegal, and punishable by law. Please download the comics **for personal use ONLY**.

>If there is an **Error** in the program, **stuck** at any point for whatever reason, have a **suggestion** for the project, please be kind enough to tell it to me in the [Issue page](https://github.com/AnonymousPomp/Comic-Downloader/issues), or emailing me at <anonymouspomp@gmail.com>. As a developer, this kind of feedbacks help me a lot, and each and every single one makes my day a bit better. : )

>If the programfails to downlaod the comics, please try using the newest version of the downloader, and if the download still doesn't work, please notify me using methods listed above.

>Some of the comics includes PG16+ contents (including PG19).

>All comics include watermarks. A watermark remover will be added in the near future

# More information
Development Environment:
- Programming Language: [Python 3.6.9](https://www.python.org)
- Designer: [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- IDE: [Pycharm](https://www.jetbrains.com/pycharm/download)

Test environment:
- [Windows 10](https://www.microsoft.com/en-us/software-download/windows10ISO)
- [Linux (Ubuntu 18.04.3 LTS)](https://ubuntu.com/download/desktop)

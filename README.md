# Comic Downloader
This is a program that downloads **Korean** (not english) web comics (AKA webtoons) from various sources.

The program is still in development, so some parts of the program may not be working properly, and features might be added and removed very rapidly.
Nothing is guaranteed until the program hits version 1.0.0

>This documentation assumes that you have the following knowledge:
>- Basic knowledge of python (python 3 to be specific)
>- How to install a python package through pip
>- Basic knowledge of terminals (cmd, bash, etc.)

# Installation
> This project requires python 3

There are two ways to run the program. You can either compile the code into and executable file, or just run the code directly.<br>
The only difference is that compiled program takes up more space and requires `cacert.pem` file to run.<br>
Compiled script usually takes up 370MB or more of the storage depending on the libraries installed.<br>
This is the reason why I decided not to upload the executable file. It's faster to compile the script than to download the executable file.

### build locally
1.) Clone the repository `git clone git@github.com:AnonymousPomp/webtoon-downloader.git`<br>
2.) Navigate to where the source code is located `cd webtoon-downloader`<br>
3.) Build package `python3 setup.py sdist bdist_wheel`<br>
4.) Navigate to where the package is built `cd dist`<br>
5.) Install package `pip install <name of the wheel file>.whl`<br>

### Install through pip
1.) Install python 3 if it's not installed
2.) run `pip install webtoondownloader`
3.) run with `webtoon-downloader` command


# Warning
>**I have no responsibility for what you do with my program**

>Downloading web comic for commercial use is illegal, and punishable by law. Please download the comics **for personal use ONLY**.

>If you have an **Error** in the program, **difficulties** at any point for whatever reason, or a **suggestion** for the project, please be kind enough to tell it to me in the [Issue page](https://github.com/AnonymousPomp/webtoon-downloader/issues), or email me at <anonymouspomp@gmail.com>. As a developer, this kind of feedbacks help me a lot, and each and every single one makes my day a bit better. : )

>If the program fails to download the comics, please try using the newest version of the downloader, and if the download still doesn't work, please notify me using methods listed above.

# More information
Development Environment:
- Programming Language: [Python 3.6.9](https://www.python.org)
- Designer: [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- IDE: [Pycharm Community edition](https://www.jetbrains.com/pycharm/download)

Tested on [Ubuntu 18.04.4 LTS](https://ubuntu.com/download/desktop)

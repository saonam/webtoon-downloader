>Read Documentation in [English](https://github.com/AnonymousPomp/Comic-Downloader) ([영어](https://github.com/AnonymousPomp/Comic-Downloader)로 도큐멘테이션 읽기)

# 웹툰 다운로더
> ## [다운로드 페이지](https://github.com/AnonymousPomp/Comic-Downloader/releases/)

이 프로그램은 여러 사이트에서 한국 웹툰을 다운받는 프로그램입니다.

프로그램은 아직 알파 버전(개발중)에 있음으로 일부 기능이 의도대로 작동하지 않을 수 있음을 알려드립니다.

인터넷 속도와 웹툰의 길이에 따라 다운로드 시간은 한 화당 10초에서 100초정도 걸립니다.

# 설치
## 윈도우
[다운로드 페이지](https://github.com/AnonymousPomp/Comic-Downloader/releases)로 가셔서 "Assets"를 클릭하시면 모든 파일이 담긴 .zip 파일을 다운로드받으실 수 있습니다.

## 리눅스
1.) 본 리포지터리를 클론합니다 `git clone https://github.com/AnonymousPomp/Comic-Downloader.git`<br>
2.) 소스 코드가 있는 디렉터리로 이동합니다 `cd Comic-Downloader/source`<br>
3.) `pyinstaller --onefile --windowed --icon=icons8-pluto-dwarf-planet-48.png ComicDownloader.py --hidden-import=queue` 커맨드를 통해 컴파일하거나 `python ComicDownloader.py` 커맨드를 통해 직접 실행하실 수 있습니다(추천) 이 방법을 선택하실 경우, 파이썬 파일을 제외한 모든 파일을 삭제하셔도 상관없습니다 (이미지 포함).

# 주의
>**여러분이 제 프로그램으로 무엇을 하든지 저에게는 책임이 없음을 알려드립니다**

>상업적인 용도로 다운받는 행위는 엄연히 불법이고, 법으로 처벌이 가능하오니, **오직** 개인 소장 용도로만 다운받아주시기 바랍니다.

>프로그램 사용 중 **오류**가 나거나, 어디에서 어떠한 이유에서든지 **막히거나**,**제안**, 혹은 **의견** 등이 있다면 [이슈 페이지](https://github.com/AnonymousPomp/Comic-Downloader/issues)에 적거나, <anonymouspomp@gmail.com>로 메일을 주시기 바랍니다. 이러한 피드백은 개발자로서 저에게 아주 많은 도움이 되며, 모든 피드백을 감사히 받도록 하겠습니다. : )

>문제가 발생할 시, [최신 버전](https://github.com/AnonymousPomp/Comic-Downloader/releases/latest)을 사용해보신 후, 여전히 작동이 되지 않는다면 위 방법으로 저에게 알려주시기 바랍니다.

>일부 웹툰들은 16금 이상의 내용을 포함하고 있사오니(19금 포함), 사용에 주의해주시기 바랍니다.

>모든 웹툰은 워터마크를 포함하고 있습니다. 워터마크 제거 프로그램은 조만간 추가될 예정입니다.

# 개발자들을 위해서
>여기서부터 나오는 모든 내용은 저의 프로그램을 사용하고 싶은 개발자들을 위한 내용들입니다. 일반 사용자들은 읽지 않으셔도 상관 없습니다.

>한국어 버전의 개발자 도큐멘테이션은 영어 버전보다 업데이트가 더디니, 영어를 알고 계신다면 위에 영어 버전을 읽으시는것을 추천드립니다

>아래 내용은 여러분이 다음을 알고 있음을 가정합니다:
>- 파이썬에 대한 중급 지식
>- 터미널에 대한 기초 지식 (bash, shell, cmd, etc.)
>- VCS(version control system) (git)에 대한 기초적인 지식
>- 기초 영어

>이 프로젝트는 [CC BY License 4.0](https://creativecommons.org/licenses/by/4.0/)에 의해 보호받고 있습니다.
>
>개발자의 citation을 유지하는 한, 변경 및 재배포등이 허용됩니다 (상업적인 용도 포함).<br>
더 자세한 정보는 [이곳](https://en.wikipedia.org/wiki/Creative_Commons_license#Types_of_licenses)을 참고하세요

개발 환경:
- 프로그래밍 언어: [파이썬 3.6.9](https://www.python.org)
- 디자이너: [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- IDE: [Pycharm](https://www.jetbrains.com/pycharm/download)

테스트 환경:
- [윈도우 10](https://www.microsoft.com/en-us/software-download/windows10ISO)
- [리눅스 (우분투) 18.04.3 LTS)](https://ubuntu.com/download/desktop)
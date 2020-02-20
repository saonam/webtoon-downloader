# python3 setup.py sdist bdist_wheel
# twine upload dist/*

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

_setup = setup(
	name="webtoondownloader",
	version="0.0.2",
	author="Anonymous Pomp",
	author_email="anonymouspomp@gmail.com",
	description="A python library for downloading and parsing Korean web comics",
	long_description=long_description,
	long_description_content_type="text/markdown",
	license="Apache-2.0",
	keywords="comic scraping webtoonscraper comicscraper webtoon web toon",
	url="https://github.com/AnonymousPomp/webtoon-scraper",
	packages=find_packages(),
	install_requires=["requests", "beautifulsoup4", "Pillow", "pyqt5", "webtoonscraper"],
	package_data={"": ["ComicGroupBox.ui", "webtoondownloader.ui"]},
	entry_points={
		'console_scripts': ['webtoon-downloader=webtoondownloader.run:main'],
	},
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Environment :: Console",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
	],
)

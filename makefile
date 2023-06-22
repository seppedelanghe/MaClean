build:
	python setup.py py2app

debug:
	python setup.py py2app
	open dist/MacClean.app/Contents/MacOS/MaClean

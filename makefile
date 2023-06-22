pack:
	rm -rf dist/ build/
	python setup.py py2app

debug:
	rm -rf dist/ build/
	python setup.py py2app
	open dist/MacClean.app/Contents/MacOS/MaClean

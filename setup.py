from setuptools import setup

APP = ['MaClean.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
    'includes': ['os'],
    'iconfile': './icon.icns',
    'resources': ['./icon.png']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

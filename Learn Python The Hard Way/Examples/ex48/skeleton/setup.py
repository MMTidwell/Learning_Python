try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author':'Mittsy Tidwell',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'mtidwell506@gamil.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectename'
}

setup(**config)


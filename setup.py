try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'gothonweb',
    'author': 'Tejovanth N',
    'url': 'https://github.com/tejovanthn/gothonweb',
    'download_url': 'https://github.com/tejovanthn/gothonweb',
    'author_email': 'tejovanthn@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'gothonweb'
}

setup(**config)

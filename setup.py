from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "PyGitio",
    version = "1.1",
    py_modules=['cli'],
    platforms = 'any',

	# metadata for upload to PyPI
    author = "ayush",
    author_email = "hsuay@outlook.com",
    description = "Command line utility to quickly shorten github links with support for custom urls.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license = "MIT",
    keywords = "gitio github url shortener shrinker",
    url = "https://github.com/hsuay/PyGitio",

    install_requires = [
        'requests',
        'Click',
        'pyperclip'
    ],

	entry_points = '''
        [console_scripts]
        pygitio=cli:main
    ''',

	project_urls = {

		'Source': 'https://github.com/hsuay/PyGitio',
		'Say Thanks!': 'https://saythanks.io/to/hsuay',
		'Buy me a coffee!': 'http://bmc.xyz/ayush'

	},


)
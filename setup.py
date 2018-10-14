from setuptools import setup, find_packages
setup(
    name = "PyGitio",
    version = "1.0",
    packages = find_packages(),
    py_modules=['pygitio'],
    platforms = 'any',

	# metadata for upload to PyPI
    author = "ayush",
    author_email = "hsuay@outlook.com",
    description = "Command line utility to quickly shorten github links with support for custom urls.",
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
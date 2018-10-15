# **PyGitio** [![PyPI](https://img.shields.io/pypi/v/nine.svg)](https://pypi.org/project/PyGitio/)

 [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

PyGitio is a cli wrapper for the git.io URL shortener with support for custom URLs.

## Installation

### Requirements
* Python 3

```
$ pip install PyGitio
```
or directly from the source, 
```
$ git clone https://github.com/hsuay/PyGitio.git && pip install -e PyGitio
```

## Usage

```
$ pygitio <GithubURL> <CustomText>
```

`<GithubURL>` is the URL that will be shortened.

`<CustomText>` is the custom text that will be used.

For example, 

```
$ pygitio https://github.com/hsuay ayush
```

This will copy the shortened URL, https://git.io/ayush to the clipboard.

<div align = "center">

![](https://duaw26jehqd4r.cloudfront.net/items/1q3T0K1W1v3O323M2j0E/Image%202018-10-15%20at%201.07.38%20PM.png)

</div>

## Dependencies

* [**Requests**](python-requests.org) - [PyPi](https://pypi.org/project/requests/) | [Repository](https://github.com/requests/requests/)
* [**Click**](https://click.palletsprojects.com) - [PyPi](https://pypi.org/project/click/) | [Repository](https://github.com/pallets/click)
* **Pyperclip** - [PyPi](https://pypi.org/project/pyperclip/) | [Repository](https://github.com/asweigart/pyperclip)

## Development
[![Feel free.](https://forthebadge.com/images/badges/fo-sho.svg)](https://media.tenor.com/images/987ccf67f8644c015d5b4bea3e51132b/tenor.gif)

```
$ virtualenv env
$ . env/bin/activate
$ pip install -e .
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://github.com/hsuay/PyGitio/blob/master/LICENSE.md)

## Mirrors

* [GitHub](https://github.com/hsuay/PyGitio)
* [BitBucket](https://bitbucket.org/hsuay/pygitio)

## Links

* [Say thanks!](https://saythanks.io/to/hsuay)
* [Buy me a coffee!](http://bmc.xyz/ayush)
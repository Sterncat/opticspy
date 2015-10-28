
##How to install and possible bugs
####Install method 1
```
$ sudo pip install opticspy
```
####Install method 2
####Download opticspy source file from [https://pypi.python.org/pypi/opticspy](https://pypi.python.org/pypi/opticspy) then
```
$ python2.7 setup.py install
```
####Possible bug when installing or later import:
####1. Error when import unwrap
####Opticspy use an [unwrap module](https://pypi.python.org/pypi/unwrap) for unwraping phase. It works well.
* ####You may get following error: [Errno 2] No such file or directory: '/Library/Python/2.7/site-packages/unwrap/__pycache__/_cffi__x8956f820xc1fce120.c'
* ####Solution: create a "\__pycache__" folder in your python package directory"/Library/Python/2.7/site-packages/unwrap/"
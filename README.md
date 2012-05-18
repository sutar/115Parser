# 115Parser

## Usage
    python 115.py file_id
where *fileId* is the segment of http://115.com/file/*fileId*

## Note
This downloader require **wget** support, which means it invokes `wget http://115_url_here` to download

## Parameter
In file 115.py, these paremeters are available to be changed:

 1.    __DOWNDIR__ = '' #where download dir located, default as current directory

 2.    __BASEURL__ = 'http://115.com/file/' # the base url of 115.com, ending with slash required

## Author
[sutar](http://wangx.in) No rights reserved. Have fun :)

## Version
 * 2012.05.18 v1.0
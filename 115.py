#! /usr/bin/env python
# Python 115 Downloader
# Usage: python 115_down.py c2ri6q0u
# where "c2ri6q0u" is the last segment of "http://115.com/file/c2ri6q0u"
# 
# 2012.5.17

import re, urllib2, sys ,os
from urllib import unquote

__BASEURL__ = 'http://115.com/file/'
__DOWNDIR__ = ''

def get_url(file_url):
	"""Get real download url"""
	page = urllib2.urlopen(__BASEURL__ + file_url, 'r').read()
	url_pattern = re.compile(r'\$\.ajax\({\s+url:\s+"/(.*)"')
	json_url = url_pattern.findall(page)[0]
	json_url = __BASEURL__ + json_url
	json_data = urllib2.urlopen(json_url).read()
	down_url_pattern = re.compile(r'data":"(.*)"')
	down_url = down_url_pattern.findall(json_data)[0].replace("\/", '/')
	return down_url

def download(down_url, referer, dest):
	"""Download file to local"""
	req = urllib2.Request(down_url)
	req.add_header('Referer', referer)
	try:
		res = urllib2.urlopen(req)
		fp = open(__DOWNDIR__ + filename, 'wb')
		fp.write(res.read())
		fp.close()
		return True
	except Exception,e:
		print 'ERROR: ',e
		return False

def download_wget(down_url, referer, dest):
	"""Download via wget"""
	os.system('wget -c --output-document="%s" --referer="%s" "%s"' % (dest ,referer, down_url))

if __name__ == '__main__':
	print 'Python 115 Downloader'
	# get file id like c2ri6q0u
	file_id = sys.argv[1].split('/')[-1] if sys.argv[1].startswith('http') else sys.argv[1]
	print 'Requested file id: %s' % file_id
	down_url = get_url(file_id)
	filename = down_url.split('file=')[-1].split('&')[0]
	save_as = __DOWNDIR__ + filename
	print 'Real url: %s' % down_url
	referer = __BASEURL__ + unquote(file_id)
	res = download_wget(down_url, referer, save_as)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @author   xds
# @date     2016-1-28
# @note     html下载器

import urllib2
from gzip import GzipFile
from cStringIO import StringIO
from jshtml.jshtml import Js_Html

class HtmlDownloader(object):
	def __init__(self):
		pass
	def download(self, url):
		headers_login={
			"Accept-Encoding":"gzip",
			"Accept-Language":"en,en-US;q=0.8,ja;q=0.6,zh-CN;q=0.4,zh;q=0.2",
			"Accept":"text/html, */*; q=0.01",
			"Content-type":"application/x-www-form-urlencoded; charset=UTF-8",
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36",
			"Referer":url,
		}

		# httpHandler = urllib2.HTTPHandler(debuglevel=1)
		# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
		request = urllib2.Request(url, headers=headers_login)
		ret = None
		code = -1
		try:
			response = urllib2.urlopen(request)
			ret=GzipFile('', 'r', 0, StringIO(response.read())).read()   
			code = 1

		except urllib2.HTTPError, e:
			code = -1
			if hasattr(e,"reason"):
				print "HTTPError: " + str(e.reason)

		except urllib2.URLError, e:
			code = -2
			if hasattr(e,"reason"):
				print "URLError: " + str(e.reason)
		return code, ret

	def set_html_by_js(self, url):
		"""
		利用casperjs来加载url，并获得解析之后的HTML内容.
		可以根据自己的需求去修改jshtml中的js代码去执行自己想要的casper
		:return:
		"""
		print u"正在启用casperjs和phantomjs进行解析,请等待......"
		code = 1
		ret = Js_Html().get_html(url)
		return code, ret
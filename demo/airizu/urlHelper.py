from urllib import urlencode
import cookielib
import urllib2
import re
import random

#Author: Henry
#Date: 2011-01-11

def getHtmlFromUrl(url):
	try:
		#print url
		header = {"User-Agent": "Mozilla-Firefox5.0"}
		page = urllib2.urlopen(url)
		#page = urlLib2.urlopen(url, header)
		html = page.read()
		page.close()
		#print html
		return html
	except:
		return ''
		
#using tor
def getHtmlFromUrlUsingTor(url):
	#try:
		#print url
		cj = cookielib.LWPCookieJar()
		cookie_support = urllib2.HTTPCookieProcessor(cj)
		
		proxy_info = {'host':'127.0.0.1', 'port':8118}
		proxy_support = urllib2.ProxyHandler({'http':'http://%(host)s:%(port)d' % proxy_info})
		
		opener = urllib2.build_opener(cookie_support, proxy_support)
		urllib2.install_opener(opener)
		
		page = urllib2.urlopen(url)
		html = page.read()
		page.close()
		#print html
		return html
	#except:
		#return ''
		
#using tor, ip, port
def getHtmlFromUrlUsingTorPort(url):
	ports = (8118,8119,8120,8121,8122,8123,8124,8125,8126,8127)
	#ports = (8118,8119,8120,8121,8122)
	port = ports[random.randint(0,len(ports)-1)]
	try:
		#print url
		cj = cookielib.LWPCookieJar()
		cookie_support = urllib2.HTTPCookieProcessor(cj)
		proxy_info = {'host':'216.139.243.53', 'port':port}
		proxy_support = urllib2.ProxyHandler({'http':'http://%(host)s:%(port)d' % proxy_info})
		
		opener = urllib2.build_opener(cookie_support, proxy_support)
		urllib2.install_opener(opener)
		
		page = urllib2.urlopen(url)
		html = page.read()
		page.close()
		print 'good port,', str(port)
		return html
	except:
		print 'fuck port,', str(port)
		return ''

def getHtmlFromLocalFile(path):
	f = open(path)
	html = f.read()
	f.close()
	return html
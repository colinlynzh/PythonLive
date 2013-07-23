# -*- coding: cp936 -*-
import StringIO
#import pycurl
import MySQLdb
import re
import sys, traceback
import time
import threading
import urllib
import random
import time
import urlHelper

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='meitian', charset='utf8')
except:
    print "Could not connect to MySQL server."
    exit(0)
#cursor = conn.cursor()
#sql = "select * from feedback"
#cursor.execute(sql)
#alldata = cursor.fetchall()
#if alldata:
    #for rec in alldata:
        #print rec[0],rec[1],rec[2]
    #print alldata
    #cursor.close()
#conn.close()
    
def usingPycurl(url):
	try:
		html = StringIO.StringIO()
		c = pycurl.Curl()
		c.setopt(pycurl.URL, url)
		#callback
		c.setopt(pycurl.WRITEFUNCTION, html.write)
		c.setopt(pycurl.FOLLOWLOCATION, 1)
		c.setopt(pycurl.MAXREDIRS, 5)
		c.setopt(pycurl.CONNECTTIMEOUT, 60)
		c.setopt(pycurl.TIMEOUT, 300)
		c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE6.0; Windows NT 5.1; SV1;.NET CLR 1.1.4322)")
		
		c.perform()	
		return html.getvalue()
	except:
		return ''

def makeSureLetyoWorkLink():
	#for i in range(1,36):
                #j= (i-1)*8
                #url = 'http://www.airizu.com/city/110100_0_0_0_0_0_0_0_0_0_1_2_1_1_8_'+str(j)+'_0.html'
                url = 'http://www.airizu.com/city/110100_0_0_0_0_0_0_0_0_0_1_2_1_1_8_0_0.html'
		html = usingPycurl(url)
		html = urlHelper.getHtmlFromUrl(url)		
		if html == '':
                        print '没有信息'
		else:
                        #print html
                        m = re.search('<p class="L">(.*?)</p>',html)
                        if m:
                            print str(m.group(1))
                        else:
                            print '不存在'

                        m1 = re.search('<a class="T js-show-item-room" target="_blank" href="/room/show/(\d).html">(.*?)</a>',html)
                        if m1:
                            print str(m1.group(1))
                        else:
                            print '不存在'
				#真正有团购信息
				#cur.execute('insert into letyo_link(id,link,link_status,created) values(%s,%s,%s,UNIX_TIMESTAMP(current_timestamp()))', (i, url, 2))
				#print 'yes'

makeSureLetyoWorkLink()


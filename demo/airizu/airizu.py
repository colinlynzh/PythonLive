#!/usr/bin/python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        fetch_airizu_content
# Purpose:
#
# Author:      Bobo <Bobo@sz.wufantuan.com>
#
# Created:     10/10/2011
# Copyright:   (c) wufantuan.com 2011
# Licence:     wufantuan.com
#-------------------------------------------------------------------------------

'''Fetch airizu.com  zufan contents'''

import time
import re
import urlHelper
import MySQLdb
import os
from BeautifulSoup import BeautifulSoup
try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='airizu', charset='utf8')
    cur = conn.cursor()
except:
    print '连接失败!'

# get the airizu.com zufan content.
def get_content(link):
    content = urlHelper.getHtmlFromUrl(link)
    return content

def insertDB(link,htmlContent):
    soup = BeautifulSoup(''.join(htmlContent))
    city_contents = soup.findAll('div',{"id":"cityPop"})
    for item in city_contents:
        city_content = item.findAll('div',{"class":"center"})
        for citys in city_content:
            city = citys.findAll('div',{"id":"ABCDF"})
            for city_item in city:
                a = city_item.findAll('a')
                for b in a:
                    b = str(b)
                    city_id = re.search('<a id="(\d+)"',b).group(1)
                    city_name = re.search('">(.*?)</a>',b).group(1)
                    url = 'http://www.airizu.com/city/'+city_id+'_0_0_0_0_0_0_0_0_0_1_2_1_1_8_0_0.html'
                    try:
                        cur.execute('select * from city where cityid = %s',(city_id))
                        rs = cur.fetchone()
                        if not rs:
                            cur.execute('insert into `city`(cityname,cityurl,cityid) values(%s,%s,%s)',(city_name,url,city_id))
                            print '添加成功'
                        else:
                            print '数据已存在'
                            continue
                    except:
                        print '添加失败'

            city = citys.findAll('div',{"id":"GHJL"})
            for city_item in city:
                a = city_item.findAll('a')
                for b in a:
                    b = str(b)
                    city_id = re.search('<a id="(\d+)"',b).group(1)
                    city_name = re.search('">(.*?)</a>',b).group(1)
                    url = 'http://www.airizu.com/city/'+city_id+'_0_0_0_0_0_0_0_0_0_1_2_1_1_8_0_0.html'
                    try:
                        cur.execute('select * from city where cityid = %s',(city_id))
                        rs = cur.fetchone()
                        if not rs:
                            cur.execute('insert into `city`(cityname,cityurl,cityid) values(%s,%s,%s)',(city_name,url,city_id))
                            print '添加成功'
                        else:
                            print '数据已存在'
                            continue
                    except:
                        print '添加失败'

            city = citys.findAll('div',{"id":"NQRS"})
            for city_item in city:
                a = city_item.findAll('a')
                for b in a:
                    b = str(b)
                    city_id = re.search('<a id="(\d+)"',b).group(1)
                    city_name = re.search('">(.*?)</a>',b).group(1)
                    url = 'http://www.airizu.com/city/'+city_id+'_0_0_0_0_0_0_0_0_0_1_2_1_1_8_0_0.html'
                    try:
                        cur.execute('select * from city where cityid = %s',(city_id))
                        rs = cur.fetchone()
                        if not rs:
                            cur.execute('insert into `city`(cityname,cityurl,cityid) values(%s,%s,%s)',(city_name,url,city_id))
                            print '添加成功'
                        else:
                            print '数据已存在'
                            continue
                    except:
                        print '添加失败'
            
            city = citys.findAll('div',{"id":"TWXYZ"})
            for city_item in city:
                a = city_item.findAll('a')
                for b in a:
                    b = str(b)
                    city_id = re.search('<a id="(\d+)"',b).group(1)
                    city_name = re.search('">(.*?)</a>',b).group(1)
                    url = 'http://www.airizu.com/city/'+city_id+'_0_0_0_0_0_0_0_0_0_1_2_1_1_8_0_0.html'
                    try:
                        cur.execute('select * from city where cityid = %s',(city_id))
                        rs = cur.fetchone()
                        if not rs:
                            cur.execute('insert into `city`(cityname,cityurl,cityid) values(%s,%s,%s)',(city_name,url,city_id))
                            print '添加成功'
                        else:
                            print '数据已存在'
                            continue
                    except:
                        print '添加失败'


#main function
def main():
    link = 'http://www.airizu.com/'
    htmlContent = get_content(link)
    insertDB(link,htmlContent)

if __name__ == '__main__':
    main()

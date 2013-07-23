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

conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='airizu', charset='utf8')
cur = conn.cursor()

# get the airizu.com zufan content.
def get_content(link):
    content = urlHelper.getHtmlFromUrl(link)
    return content

def get_zufanginfo(link):
    content = urlHelper.getHtmlFromUrl(link)
    return content

def get_pagenumber(link):
    p = 0
    content = urlHelper.getHtmlFromUrl(link)
    if content:
        soup = BeautifulSoup(''.join(content))
        if soup:
            page_content = soup.findAll('div',{"class":"page js-page"})[0]
            page_content =str(page_content)
            page_numb = re.search('<span class="step">..</span><a (.*?) class="step">(\d+)</a><a (.*?) class="nextLink">下页</a>',page_content,re.S)
            if page_numb:
                p = page_numb.group(2)
                return p
            else:
                return 0
        else:
            return 0
    else:
        return 0

housetype = '家庭旅馆'
roomnumber = 1
bedtype = '单人床'
bathrooms = 1
mindays = 1
maxdays = '不限'
checkintime = '灵活的'
checkouttime = '灵活的'
area = 0
def insertDB(link,htmlContent,cityname):
    cityname = cityname
    global housetype
    global roomnumber
    global bedtype
    global bathrooms
    global mindays
    global maxdays
    global checkintime
    global checkouttime
    global area
    if htmlContent:
        soup = BeautifulSoup(''.join(htmlContent))
        deal_content = soup.findAll('ul',{"class":"RL"})
        for item in deal_content:
            deal_li = item.findAll('li',{"class":"js-search-result"})
            for li in deal_li:
                #url地址
                url = 'http://www.airizu.com'+li.div.a['href']

                x = li.input['id']
                y = li.input['name']

                #title标题
                titles  = str(li.findAll("a",{"class":"T js-show-item-room"})[0])
                title = re.search('<a href="/room/show/(\d+)\.html" class="T js-show-item-room" target="_blank">(.*?)</a>',titles)
                if title:
                    title = title.group(2)

                #address 地址
                addresss = str(li.findAll("p",{"class":"L"})[0])
                address = re.search('<p class="L">(.*?)</p>',addresss)
                if address:
                    address = address.group(1)

                #价格
                prices = str(li.findAll('p',{"class":"number"}))
                price = re.search('<p class="number">(\d+)</p>',prices)
                if price:
                    price = price.group(1)

                #房间类型
                roomtypes = str(li.findAll('div',{"class":"erect_icon fs"}))
                roomtype = re.search('<div class="erect_icon fs">(.*?)</div>',roomtypes)
                if roomtype:
                    roomtype = roomtype.group(1)

                #可住人数
                numberss = str(li.findAll('div',{"class":"erect_icon rs"}))
                numbers = re.search('<div class="erect_icon rs">(\d+)人</div>',numberss)
                if numbers:
                    numbers = numbers.group(1)

                #根据URL获取租房详细信息----
                zufang_content = get_zufanginfo(url)
                zufang_soup = BeautifulSoup(''.join(zufang_content))
                zufang_infos = zufang_soup.findAll('div',{"class":"main room_page"})
                for zufang_info in zufang_infos:
                    #房间描述
                    discriptions = str(zufang_info.findAll('div',{"class":"room_description"})[0])
                    discription = re.search('<div class="room_description">(.*?)</div>',discriptions)
                    if discription:
                        discription = discription.group(1)

                    #配套设施
                    facilities = ''
                    facilitiess = zufang_info.findAll('li',{"class":"has_not"})
                    for li in facilitiess:
                        li = str(li)
                        facilities_info = re.search('<li class="has_not">(.*?)</li>',li)
                        if facilities_info:
                            facilities_info = facilities_info.group(1)
                            facilities = facilities + facilities_info+','

                    #房屋使用规则
                    rule='<p>* 入住时请您准备您入住的全部房租费用和押金，如果您事先支付了租房定金，我们将会把您支付的租房定金充抵房租。我们不接受退房时交费，请谅解！</p>\
                    <p>* 您必须带好您的有效身份证件，对于没有证件者，我们一概不接待。</p>\
                    <p>* 承租手续办完后，我方管理人员不会擅自进入您的房间，如遇特殊情况，我们会事先与您取得联系,经您的允许后管理人员方可进入您的房间(遇紧急情况除外)。</p>\
                    <p>* 网上公布的房租不含发票，如需开发票另加6%的税率。</p>'

                    room_detailss = zufang_info.findAll('div',{"class":"room_details"})
                    for room_details in room_detailss:
                        trs = room_details.findAll('tr')
                        for tr in trs:
                            #房屋类型----
                            housetypes = re.search('<th>房屋类型：<\/th>(\n)<td>(.*?)<\/td>',str(tr))
                            if housetypes:
                                housetype = housetypes.group(2)

                            #卧室数-------
                            roomnumbers = re.search('<th>卧室数：<\/th>(\n)<td>(.*)<\/td>',str(tr))
                            if roomnumbers:
                                roomnumber = roomnumbers.group(2)

                            #床型-------
                            bedtypes = re.search('<th>床型：<\/th>(\n)<td>(.*)<\/td>',str(tr))
                            if bedtypes:
                                bedtype = bedtypes.group(2)

                            #卫生间数-------
                            bathroomss = re.search('<th>卫生间数：<\/th>(\n)<td>(.*)<\/td>',str(tr))
                            if bathroomss:
                                bathrooms = bathroomss.group(2)

                            #最少天数-------
                            mindayss = re.search('<th>最少天数：<\/th>(\n)<td>(.*)<\/td>',str(tr))
                            if mindayss:
                                mindays = mindayss.group(2)

                            #最多天数-------
                            maxdayss = re.search('<th>最多天数：<\/th>(\n)<td>(.*)<\/td>',str(tr))
                            if maxdayss:
                                maxdays = maxdayss.group(2)

                            #入住时间-------
                            checkintimes = re.search('<th>入住时间：<\/th>(\n)<td>(.*)<\/td>',str(tr))
                            if checkintimes:
                                checkintime = checkintimes.group(2)

                            #退房时间-------
                            checkouttimes = re.search('<th>退房时间：<\/th>(\n)<td>(.*)<\/td>',str(tr))
                            if checkouttimes:
                                checkouttime = checkouttimes.group(2)

                            #面积-------
                            areas = re.search('<th>面积：<\/th>(\n)<td>(\d+)平方米<\/td>',str(tr))
                            if areas:
                                area = areas.group(2)
                    
                        
                #根据URL获取租房详细信息----

                #查询记录是否存在,不存在入库----
                try:
                    cur.execute('select * from zf_message where url = %s',(url))
                    rs = cur.fetchone()
                    if not rs:
                        cur.execute('insert into `zf_message` (cityname,url,title,address,numbers,price,roomtype,discription,facilities,rule,housetype,roomnumber,\
                        bedtype,bathrooms,mindays,maxdays,checkintime,checkouttime,area,x,y) \
                        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(cityname,url,title,address,numbers,price,roomtype,discription,facilities,rule,housetype,roomnumber,bedtype,bathrooms,mindays,maxdays,checkintime,checkouttime,area,x,y))
                        print '1111!'
                    else:
                        print '3333'
                except:
                    print '2222!'

     


#init the page && totalPage
page      = 0
totalPage = 37

#main function
def main():
    global page
    global totalPage
    cur.execute('select * from city')
    rs = cur.fetchall()
    if rs:
        for item in rs:
            cityname = item[1]
            cityurl = item[2]
            cityid = item[3]
            maxpage = get_pagenumber(cityurl)
            totalPage = int(maxpage)
            print totalPage
            if maxpage > 0:
                while True:
                    page  = page + 1
                    j = (page-1)*8
                    link = 'http://www.airizu.com/city/'+cityid+'_0_0_0_0_0_0_0_0_0_1_2_1_1_8_'+str(j)+'_0.html'
                    htmlContents = get_content(link)
                    insertDB(link,htmlContents,cityname)
                    #exit the while 
                    if page == totalPage :
                        continue
        
    return 0

if __name__ == '__main__':
    main()

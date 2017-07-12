# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:46:34 2017

@author: Linzhe
"""

import urllib
import urllib2
import re
import pandas as pd
import time

resp_list = []
column = 'szse'
pageSize = 30
searchkey = "异常波动;"
columnTitle = '历史公告查询'
tabName = 'fulltext'
showTitle = "-1/searchkey/异常波动"
seDate = "请选择日期"
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
headers = { 'User-Agent' : user_agent }
url = 'http://www.cninfo.com.cn/cninfo-new/announcement/query'
pn = 1
has_more=True

while has_more:
    values = {'searchkey':searchkey, 'tabName':tabName, 'columnTitle':columnTitle, 'column':column, 'pageNum':pn, 'pageSize':pageSize, 'showTitle':showTitle, 'seDate':seDate}
    jdata = urllib.urlencode(values)
    req = urllib2.Request(url,jdata,headers)
    response = urllib2.urlopen(req)
    resp = response.read()
    has_more = re.findall(r'.*?\"hasMore\":tru(.*?)}',resp)
    resp_list.append(resp)
    pn = pn+1
    print jdata
    print '————————————>>>'+str(pn-1)+'>>>————————————'
    print has_more
    time.sleep(1)


str_list = "".join(resp_list)
li = open('C://Users//Linzhe//Desktop//Intern//Quant//shijianku//YiChangBoDong//data//' + 'Notice_YiChangBoDong','w+')
li.write(str_list)
li.close()


code_list = []
name_list = []
time_list = []
announcementTitle_list = []
for i in range(len(resp_list)):
    code_list.extend(re.findall(r'"secCode":(.+?),"secName"',resp_list[i]))
    name_list.extend(re.findall(r'"secName":"(.+?)","orgId"',resp_list[i]))
    time_list.extend(re.findall(r'"announcementTime":(.+?),"adjunctUrl"',resp_list[i]))
    announcementTitle_list.extend(re.findall(r'"announcementTitle":"(.+?)","announcementTime"',resp_list[i]))

l=[code_list, name_list, time_list, announcementTitle_list]
t=zip(*l)
tt=pd.DataFrame(t)
fun = lambda x: time.strftime('%Y%m%d', time.localtime(float(x)/1000))#将13位时间戳转换成标准日期格式
tt[2] = tt[2].apply(fun)
header=['股票代码', '股票简称', '公告日期','公告标题']
tt.to_csv('Announcement_YiChangBoDong.csv',encoding='gbk',header=header,index=False)



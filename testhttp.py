#!/usr/bin/python
# coding=utf-8

import urllib3
import datetime
import time
import urllib

# 创建连接特定主机的连接池
http_pool = urllib3.HTTPConnectionPool('ent.qq.com')
# 获取开始时间
now = time.localtime(time.time())
strStart = time.strftime("%Y/%m/%d %H:%M:%S", now)

for i in range(0, 100, 1):
    print(i)
    # 组合URL字符串
    url = 'http://ent.qq.com/a/20111216/%06d.htm' % i
    print(url)

    # 开始同步获取内容
    r = http_pool.urlopen('GET', url, redirect=False)
    print(r.status, r.headers, len(r.data))

# 打印时间
print('start time : ', strStart)

now = time.localtime(time.time())
strEnd = time.strftime("%Y/%m/%d %H:%M:%S", now)
print('end time : ', strEnd)

#!/usr/bin/python
# coding=utf-8

import time

tstart = '2017/06/08 17:06:00'
startTimeArray = time.strptime(tstart, "%Y/%m/%d %H:%M:%S")

mktime = time.mktime(startTimeArray) * 1000
tstart = str(int(round(mktime)))
print(tstart)

now = time.localtime(time.time())
now_str = time.strftime("%Y/%m/%d %H:%M:%S", now)
print(now_str)

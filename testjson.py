#!/usr/bin/python
# coding=utf-8

import json

# 字符串转对象
str = '{"app":{"name":"九块九"},"device":{"imei":"3242342342342"}}'

data = json.loads(str)

print(data['app']['name'])
print(data['device']['imei'])

# 对象转字符串
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

# 构造对象，转字符串
data2 = {}
app = {}
device = {}

app['name'] = '九块九'
device['imei'] = '3242342342342'

data2['app'] = app
data2['device'] = device

json_str2 = json.dumps(data2, ensure_ascii=False)
print(json_str2)

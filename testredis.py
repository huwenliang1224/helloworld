#!/usr/bin/python
# coding=utf-8

import redis

db = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

db.set('name', '你好')

b = db.get('name')

print(b.decode('utf-8'))

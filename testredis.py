#!/usr/bin/python
# coding=utf-8

# import redis

# db = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
#
# db.set('name', '你好')
#
# b = db.get('name')
#
# print(b.decode('utf-8'))ls

import RedisUtil
import logger
import sys
import operator

try:
    if (len(sys.argv) != 2):
        raise Exception('no param')

    arg = sys.argv[1]

    if (not operator.eq(arg, 'true') and not operator.eq(arg, 'false')):
        raise Exception('param:true/false')

    isCluster = False

    if (operator.eq(arg, 'true')):
        isCluster = True

    redis = RedisUtil.newInstance(isCluster)

    # redis.set('name', '你好吗')

    redis.hset('toutiao.area.areas', '上海', '')
    redis.hset('toutiao.area.areas', '北京', '')
    list = redis.hgetAll('toutiao.area.areas')
    for area in list:
        print(area)

    # print(redis.get('name'))
except Exception as e:
    print("error:" + e.args[0])

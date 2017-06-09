#!/usr/bin/python
# coding=utf-8

import redis
from rediscluster import RedisCluster


class newInstance:
    def __init__(self, isCluster):
        try:
            self.isCluster = isCluster;
            if (isCluster):
                startup_nodes = [{"host": "192.168.234.229", "port": "7000"}]
                self.redis = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
            else:
                self.redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
            self.redis.ping()
        except:
            raise Exception('redis connection error')

    def get(self, key):
        try:
            val = self.redis.get(key)
            if val is not None:
                if(self.isCluster):
                    return val
                else:
                    return val.decode('utf-8')
            else:
                return ''
        except:
            raise Exception('get error')

    def set(self, key, value):
        try:
            self.redis.set(key, value)
        except:
            raise Exception('set error')

    def delete(self, key):
        try:
            self.redis.delete(key)
        except:
            raise Exception('delete error')

    def hset(self, table, key, value):
        try:
            self.redis.hset(table, key, value)
        except:
            raise Exception('hset error')

    def hget(self, table, key):
        try:
            val = self.redis.hget(table, key)
            if val is not None:
                if (self.isCluster):
                    return val
                else:
                    return val.decode('utf-8')
            else:
                return ''
        except:
            raise Exception('hget error')

    def hdel(self, table, key):
        try:
            return self.redis.hdel(table, key)
        except:
            raise Exception('hdel error')

    def hgetAll(self, table):
        try:
            val = self.redis.hgetall(table)
            if val is not None:
                list = []
                for (k, v) in val.items():
                    if (self.isCluster):
                        list.append(k)
                    else:
                        list.append(k.decode('utf-8'))

                return list
            else:
                return []
        except:
            raise Exception('hgetAll error')

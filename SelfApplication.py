#!/usr/bin/python
# coding=utf-8

import operator
import sys

import StrategyManager

def main():
    if (len(sys.argv) == 0):
        print("commands: gen/update/drop/set/get/del/hset/hget/hdel/hgetall")
        sys.exit(0)

    isCluster = sys.argv[2]

    if (not operator.eq(isCluster, 'true') and not operator.eq(isCluster, 'false')):
        print("arg[1] true/false(whether use cluster)")
        sys.exit(0)

    isCluster = True if operator.eq(isCluster, 'true') else False

    command = sys.argv[1]

    if (operator.eq(command, 'gen')):
        if (len(sys.argv) == 4):
            try:
                snum = sys.argv[3]
                StrategyManager.generateStrategy(isCluster, False, snum)
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("init command : gen 001/002/../00n(stragety num)")
            sys.exit(0)
    elif (operator.eq(command, 'update')):
        if (len(sys.argv) == 4):
            try:
                snum = sys.argv[3]
                StrategyManager.generateStrategy(isCluster, True, snum)
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("init command : gen 001/002/../00n(stragety num)")
            sys.exit(0)
    elif (operator.eq(command, 'drop')):
        if (len(sys.argv) == 4):
            try:
                snum = sys.argv[3]
                StrategyManager.drop(isCluster, snum)
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("init command : drop 001/002/../00n(stragety num)")
            sys.exit(0)
    elif (operator.eq(command, 'look')):
        if (len(sys.argv) == 4):
            try:
                snum = sys.argv[3]
                StrategyManager.look(isCluster, snum)
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("init command : look 001/002/../00n(stragety num)")
            sys.exit(0)
    elif (operator.eq(command, 'set')):
        if (len(sys.argv) == 5):
            try:
                key = sys.argv[3];
                value = sys.argv[4];
                import RedisUtil
                redis = RedisUtil.newInstance(isCluster)
                redis.set(key, value)
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("set command : set key(String) value(String)")
            sys.exit(0)
    elif (operator.eq(command, 'get')):
        if (len(sys.argv) == 4):
            try:
                key = sys.argv[3];
                import RedisUtil
                redis = RedisUtil.newInstance(isCluster)
                print(redis.get(key))
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("get command : get key(String)")
            sys.exit(0)
    elif (operator.eq(command, 'del')):
        if (len(sys.argv) == 4):
            try:
                key = sys.argv[3];
                import RedisUtil
                redis = RedisUtil.newInstance(isCluster)
                redis.delete(key)
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("del command : get key(String)")
            sys.exit(0)
    elif (operator.eq(command, 'hset')):
        if (len(sys.argv) == 6):
            try:
                table = sys.argv[3];
                key = sys.argv[4];
                value = sys.argv[5];
                import RedisUtil
                redis = RedisUtil.newInstance(isCluster)
                redis.hset(table, key, value);
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("hset command : get key(String)")
            sys.exit(0)
    elif (operator.eq(command, 'hget')):
        if (len(sys.argv) == 5):
            try:
                table = sys.argv[3];
                key = sys.argv[4];
                import RedisUtil
                redis = RedisUtil.newInstance(isCluster)
                print(redis.hget(table, key))
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("hget command : set key(String) value(String)")
            sys.exit(0)
    elif (operator.eq(command, 'hdel')):
        if (len(sys.argv) == 5):
            try:
                table = sys.argv[3];
                key = sys.argv[4];
                import RedisUtil
                redis = RedisUtil.newInstance(isCluster)
                print(redis.hdel(table, key))
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("hdel command : set key(String) value(String)")
            sys.exit(0)
    elif (operator.eq(command, 'hgetall')):
        if (len(sys.argv) == 4):
            try:
                table = sys.argv[3];
                import RedisUtil
                redis = RedisUtil.newInstance(isCluster)
                print(redis.hgetAll(table))
            except Exception as e:
                print(e)
                sys.exit(0)
        else:
            print("hgetall command : get key(String)")
            sys.exit(0)
    else:
        print("commands: switch/init/set/get/del/hset/hget")
        sys.exit(0)


if __name__ == '__main__':
    main()

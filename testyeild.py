#!/usr/bin/python
# coding=utf-8

list = range(10)

def multiply2(list):
    for i in list:
        yield i * 2

list2 = multiply2(list)

for i in list2:
    print(i)


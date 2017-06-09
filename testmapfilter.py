#!/usr/bin/python
# coding=utf-8

symbols = '$¢£¥€¤'

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

list1 = [1, 2, 3]

func_mul = lambda x: x * 100
func_fil = lambda x: x > 100

print(list(filter(func_fil, map(func_mul, list1))))

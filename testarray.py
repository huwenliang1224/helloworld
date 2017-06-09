#!/usr/bin/python
# coding=utf-8

import array

a1 = [1, 2, 3]
a2 = [4, 5, 6]

a = array.array('d', a1)
b = array.array('d', a2)

print(a.tolist())
print(b.tolist())

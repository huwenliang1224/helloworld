#!/usr/bin/python
# coding=utf-8

import bisect

data = [5, 3, 8, 2, 9, 12]
print(data)

data.sort()
print(data)

bisect.insort(data, 4)
print(data)

index = bisect.bisect(data, 2)
print(index)

print(data)

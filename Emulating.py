#!/usr/bin/python
# coding=utf-8

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

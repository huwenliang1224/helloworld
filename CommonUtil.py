#!/usr/bin/python
# coding=utf-8

def isNotBlank(value):
    return value is not None and len(value) > 0

def isBlank(value):
    return value is None or len(value) == 0

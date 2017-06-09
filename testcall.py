#!/usr/bin/python

class Test():
    def __init__(self):
        pass

    def p(self):
        print('hello')

    def __call__(self, *args, **kwargs):
        return self.p()

test = Test()
test.p()
test()

print(callable(test))
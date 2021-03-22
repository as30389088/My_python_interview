# -*- coding: utf-8 -*-
__author__ = "lei"


a, b, c, d = 1, 1, 1000, 1000
print(a is b, c is d)


def foo():
    e = 1000
    f = 1000
    print(e is f, e is d)
    g = 1
    print(g is a)

foo()


"""
第一个print 是True, False
第二个print 是True, False
第三个print 是True

其中 a is b 为True  c is d 为 False,因为Cpython对频繁出现的整数设定small_ints的缓存池，small_ints中的设定的缓存整数值为[-5, 256]之间
所以 a, b 对应的会是一个对象的id，c,d 是两个对象的id

其他同理



"""
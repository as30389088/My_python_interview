# -*- coding: utf-8 -*-
__author__ = "lei"


# 面试中经常让写生成斐波那契数列的迭代器，大家可以参考下面的代码。
class Fib(object):

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


fib = Fib(10)
print(list(fib))    # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# for i in range(10):
#     print(fib.__next__())


# 如果用生成器的语法来改写上面的代码，代码会简单优雅很多。

def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a
# -*- coding: utf-8 -*-
__author__ = "lei"


test_list = [1,1,1,2,2,2,3,3,3,4,4,5,5,6,7]


def dup_func(x: list):
    res_list = []
    x_set = set()
    for i in x:
        if i not in x_set:
            res_list.append(i)
            x_set.add(i)
    return res_list

# 改造生成器

def dup_yield_func(x: list):
    x_set = set()
    for i in x:
        if i not in x_set:
            yield i
            x_set.add(i)

print(test_list)
print(dup_func(test_list))
print(list(dup_yield_func(test_list)))
print(dup_yield_func(test_list))

"""
扩展：由于Python中的集合底层使用哈希存储，所以集合的in和not in成员运算在性能上远远优于列表，
所以上面的代码我们使用了集合来保存已经出现过的元素。集合中的元素必须是hashable对象，
因此上面的代码在列表元素不是hashable对象时会失效，要解决这个问题可以给函数增加一个参数，
该参数可以设计为返回哈希码或hashable对象的函数。
"""
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


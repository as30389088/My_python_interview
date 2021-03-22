# -*- coding: utf-8 -*-
__author__ = "lei"

###### 001 python 中如何实现单例模式

# 方法一：使用装饰器实现单例模式

from functools import wraps


def singleton(cls):
    """
    单例类装饰器
    :param cls:
    :return:
    """
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    pass


President()
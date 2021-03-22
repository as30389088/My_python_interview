# -*- coding: utf-8 -*-
__author__ = "lei"


"""
单例模式一般应用于一个对象的状态是被其他对象共享的
eg: 数据库连接池
    项目日志的操作
"""

###### 001 python 中如何实现单例模式

# 方法一：使用装饰器实现单例模式

from functools import wraps


# def singleton(cls):
#     """
#     单例类装饰器
#     :param cls:
#     :return:
#     """
#     instances = {}
#
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
#
# @singleton
# class President:
#     pass


# President()


# #### 方法二 使用元类实现单例模式

class SingletonMeta(type):
    """
    自定义单例元类
    """
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    pass
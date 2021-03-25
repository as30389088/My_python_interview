# -*- coding: utf-8 -*-
__author__ = "lei"

import os

g = os.walk(r"D:\Python面试宝典")


#  walk  返回 文件的绝对路径  路径下的文件夹数   路径下的文件数
for path, dir_list, file_list in g:
    for dir_name in dir_list:
        print(os.path.join(path, dir_name))

    for file_name in file_list:
        print(os.path.join(path, file_name))
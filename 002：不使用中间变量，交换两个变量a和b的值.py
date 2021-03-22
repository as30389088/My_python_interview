# -*- coding: utf-8 -*-
__author__ = "lei"


#### 方法一

a = '123'
b = '456'

print('a', a)
print('b', b)

a, b = b, a
print('交换a的值后', a)
print('交换b的值后', b)


"""
扩展：需要注意，a, b = b, a这种做法其实并不是元组解包，虽然很多人都这样认为。
Python字节码指令中有ROT_TWO指令来支持这个操作，类似的还有ROT_THREE，对于3个以上的元素，
如a, b, c, d = b, c, d, a，才会用到创建元组和元组解包。想知道你的代码对应的字节码指令，
可以使用Python标准库中dis模块的dis函数来反汇编你的Python代码
"""
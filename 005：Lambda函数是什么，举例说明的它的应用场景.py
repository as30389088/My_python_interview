# -*- coding: utf-8 -*-
__author__ = "lei"


"""点评：这个题目主要想考察的是Lambda函数的应用场景，潜台词是问你在项目中有没有使用过Lambda函数，
具体在什么场景下会用到Lambda函数，借此来判断你写代码的能力。因为Lambda函数通常用在高阶函数中，
主要的作用是通过向函数传入函数或让函数返回函数最终实现代码的解耦合。

Lambda函数也叫匿名函数，它是功能简单用一行代码就能实现的小型函数。Python中的Lambda函数只能写一个表达式，
这个表达式的执行结果就是函数的返回值，不用写return关键字。Lambda函数因为没有名字，所以也不会跟其他函数发生命名冲突的问题。

扩展：面试的时候有可能还会考你用Lambda函数来实现一些功能，也就是用一行代码来实现题目要求的功能，
例如：用一行代码实现求阶乘的函数，用一行代码实现求最大公约数的函数等。"""

fac = lambda x: __import__('functools').reduce(int.__mul__, range(1, x + 1), 1)
gcd = lambda x, y: y % x and gcd(y % x, x) or x
"""Lambda函数其实最为主要的用途是把一个函数传入另一个高阶函数（如Python内置的filter、map等）中来为函数做解耦合，
增强函数的灵活性和通用性。下面的例子通过使用filter和map函数，实现了从列表中筛选出奇数并求平方构成新列表的操作，
因为用到了高阶函数，过滤和映射数据的规则都是函数的调用者通过另外一个函数传入的，
因此这filter和map函数没有跟特定的过滤和映射数据的规则耦合在一起。"""

# TODO filter()  函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表


items = [12, 5, 7, 10, 8, 19]
filter_list = list(filter(lambda x: x % 2, items))
print(filter_list)
items = list(map(lambda x: x ** 2, filter(lambda x: x % 2, items)))
print(items)    # [25, 49, 361]
# 扩展：用列表的生成式来实现上面的代码会更加简单明了，代码如下所示。

items = [12, 5, 7, 10, 8, 19]
items = [x ** 2 for x in items if x % 2]
print(items)    # [25, 49, 361]
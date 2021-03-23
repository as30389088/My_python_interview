# -*- coding: utf-8 -*-
__author__ = "lei"


# 点评：这个题目本身出现的频率非常高，但是就题论题而言没有什么技术含量。对于这种面试题，
# 在回答的时候一定要让你的答案能够超出面试官的预期，这样才能获得更好的印象分。
# 所以回答这个题目的要点不仅仅是能够说出浅拷贝和深拷贝的区别，深拷贝的时候可能遇到的两大问题，
# 还要说出Python标准库对浅拷贝和深拷贝的支持，然后可以说说列表、字典如何实现拷贝操作以及如何通过序列化和反序列的方式实现深拷贝，
# 最后还可以提到设计模式中的原型模式以及它在项目中的应用。
#
# 浅拷贝通常只复制对象本身，而深拷贝不仅会复制对象，还会递归的复制对象所关联的对象。
# 深拷贝可能会遇到两个问题：一是一个对象如果直接或间接的引用了自身，会导致无休止的递归拷贝；
# 二是深拷贝可能对原本设计为多个对象共享的数据也进行拷贝。Python通过copy模块中的copy和deepcopy函数来实现浅拷贝和深拷贝操作，
# 其中deepcopy可以通过memo字典来保存已经拷贝过的对象，从而避免刚才所说的自引用递归问题；
# 此外，可以通过copyreg模块的pickle函数来定制指定类型对象的拷贝行为。
#
# deepcopy函数的本质其实就是对象的一次序列化和一次返回序列化，面试题中还考过用自定义函数实现对象的深拷贝操作，
# 显然我们可以使用pickle模块的dumps和loads来做到，代码如下所示。

import pickle

my_deep_copy = lambda obj: pickle.loads(pickle.dumps(obj))
# 列表的切片操作[:]相当于实现了列表对象的浅拷贝，而字典的copy方法可以实现字典对象的浅拷贝。
# 对象拷贝其实是更为快捷的创建对象的方式。在Python中，通过构造器创建对象属于两阶段构造，首先是分配内存空间，然后是初始化。
# 在创建对象时，我们也可以基于“原型”对象来创建新对象，通过对原型对象的拷贝（复制内存）就完成了对象的创建和初始化，
# 这种做法更加高效，这也就是设计模式中的原型模式。在Python中，我们可以通过元类的方式来实现原型模式，代码如下所示。

import copy


class PrototypeMeta(type):
    """实现原型模式的元类"""

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为对象绑定clone方法来实现对象拷贝
        cls.clone = lambda self, is_deep=True: \
            copy.deepcopy(self) if is_deep else copy.copy(self)


class Person(metaclass=PrototypeMeta):
    pass


p1 = Person()
p2 = p1.clone()                 # 深拷贝
p3 = p1.clone(is_deep=False)    # 浅拷贝
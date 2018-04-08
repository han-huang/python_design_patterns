# -*- coding: utf-8 -*-

# http://tw.dlxedu.com/detail/5/496860.html
# http://blog.csdn.net/azsx02/article/details/77649527
# https://read01.com/n4nJPk.html


def lazy_property(func):
    attr_name = '_lazy_' + func.__name__

    @property
    def _lazy_property(self):  
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self)) #self->c, attr_name->_lazyarea, func->area()
        return getattr(self, attr_name)
    return _lazy_property

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    @lazy_property
    def area(self):
        print('evalute')
        return 3.14*self.radius ** 2  

c = Circle(4)
print(c.__dict__)
c.area
print(c.__dict__)

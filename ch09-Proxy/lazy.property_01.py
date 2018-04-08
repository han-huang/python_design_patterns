# -*- coding: utf-8 -*-

# http://tw.dlxedu.com/detail/5/496860.html
# http://blog.csdn.net/azsx02/article/details/77649527
# https://read01.com/n4nJPk.html

class lazy(object):
    def __init__(self, func):   
        self.func = func #lazy的實例屬性func等於area方法物件

    def __get__(self, instance, cls):   
        val = self.func(instance) #調用area方法計算出結果
        setattr(instance, self.func.__name__, val) #將結果設置給c的area屬性
        return val

class Circle(object):   
    def __init__(self, radius):   
        self.radius = radius   

    @lazy #area = lazy(area) lazy描述符
    def area(self):   
        print('evalute')
        return 3.14 * self.radius ** 2 

c = Circle(4)   
print(c.radius)
print(c.area)
print(c.area)
print(c.area)


# 結果'evalute'只輸出了一次。在lazy類中，我們定義了__get__方法，所以它是一個描述符。
# 當我們第一次執行c.area時，python解釋器會先從c.__dict__中進行查找，沒有找到，就從
# Circle.__dict__中進行查找，這時因為area被定義為描述符，所以調用__get__方法。
# 在__get__方法中，調用實例的area方法計算出結果，並動態給實例添加一個同名屬性area，
# 然後將計算出的值賦予給它，相當於設置c.__dict__['area']=val。當我們再次調用c.area時
# ，直接從c.__dict__中進行查找，這時就會直接返回之前計算好的值了。

# Output
# 4
# evalute
# 50.24
# 50.24
# 50.24

# coding: utf-8


class LazyProperty:

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print('function overriden: {}'.format(self.method))
        print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):
        print('obj {}'.format(obj))
        if not obj:
            return None
        print('before: value = self.method(obj)')
        value = self.method(obj) # call resource()
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        print('setattr {} {}'.format(self.method_name, value))
        return value

class Test:

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))    # 假設這一行的計算成本比較大
        return self._resource

# http://tw.dlxedu.com/detail/5/496860.html
# http://blog.csdn.net/azsx02/article/details/77649527
# https://read01.com/zh-tw/n4nJPk.html#.WpxOuehuZPY
# 我們第一次執行t.resource時，python解釋器會先從t.__dict__中進行查找，沒有找到，就從Test.__dict__中進行查找，
# 這時因為resource被定義為描述符，所以調用__get__方法。在__get__方法中，調用實例的resource方法計算出結果，
# 並動態給實例添加一個同名屬性resource，然後將計算出的值賦予給它，相當於設置t.__dict__['resource']=val。
# 當我們再次調用t.resource時，直接從t.__dict__中進行查找，這時就會直接返回之前計算好的值了。

def main_Py27():
    # python 2.7.x
    t = Test()
    print(t.x)
    #>>> foo
    print(t.y)
    #>>> bar
    print(t.resource)
    #>>> <__main__.LazyProperty instance at 0x02C2E058>
    print(t.resource.__get__(t,Test))
    #>>> initializing self._resource which is: None
    #>>> (0, 1, 2, 3, 4)
    print(t.resource)
    #>>> (0, 1, 2, 3, 4)
    
def main_Py3():
    # python 3.x
    print(main_Py3.__name__)
    # print('dir(Test): ', dir(Test))
    t = Test()
    print(t.x)
    #>>> foo
    print(t.y)
    #>>> bar
    print(t.resource)
    #>>> before: value = self.method(obj)
    #>>> initializing self._resource which is: None
    #>>> (0, 1, 2, 3, 4)
    print(t.resource)
    #>>> (0, 1, 2, 3, 4)

    # print("After calling t.resource, t has new attributes: ", set(dir(t))-set(dir(Test))) #  {'y', '_resource', 'x'} -> def __init__(self)
    # print('dir(t): ', dir(t))

def main():
    import sys
    if sys.version_info < (3,0):
        main_Py27()
    else:
        main_Py3()

if __name__ == '__main__':
    main()

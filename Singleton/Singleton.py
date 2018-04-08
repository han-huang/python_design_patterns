# http://www.zlovezl.cn/articles/__init__-and__new__-in-python/

class Singleton(object):
    def __new__(cls):
        # 關鍵在於這，每一次產生實體的時候，我們都只會返回這同一個instance物件
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value1'
print(obj1.attr1, obj2.attr1) # value1 value1
print(obj1 is obj2) # True

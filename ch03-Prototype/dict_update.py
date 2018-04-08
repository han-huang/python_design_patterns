# http://www.cnblogs.com/hhh5460/p/5579478.html
# 一行式構造器

class Test():
    # 初始化
    def __init__(self, a, b, c=2, d=3, e=4, f=5):
        self.__dict__.update({k:v for k,v in locals().items() if k != 'self'})
    
    # 設置
    def set_option(self, *args, **kwargs):
        self.__dict__.update(dict(zip('abcdef'[:len(args)], args))) # args 必須按__init__的順序！
        self.__dict__.update(**kwargs)
        
    # 別的方法
    def show(self):
        print(self.__dict__)
    
    
t = Test(0, 1)
t.show()
t.set_option(100, 99, 98, 97, f=96, e=95)
t.show()

# >>> args = (100, 99, 98, 97)
# >>> 'abcdef'[:len(args)]
# 'abcd'

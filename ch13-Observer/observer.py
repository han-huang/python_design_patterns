class Publisher:

    def __init__(self):
        self.observers = [] # 觀察者列表

    def add(self, observer): # 添加觀察者
        if observer not in self.observers: # 如果觀察者不在列表中
            self.observers.append(observer) # 向列表中添加觀察者
        else: # 否則，觀察者已經在列表中，已經在觀察，為避免多次 notify
            print('Failed to add: {}'.format(observer)) # 添加失敗提示

    def remove(self, observer): # 移除觀察者
        try: #　嘗試
            self.observers.remove(observer) # 從列表移除觀察者
        except ValueError: # 如果觀察者不在列表中，引發值異常
            print('Failed to remove: {}'.format(observer)) # 移除失敗提示

    def notify(self): # 通知所有觀察者，狀態已經改變
        # 通知清單中的每一個觀察值，狀態已經改變
        [o.notify(self) for o in self.observers] 
        

class DefaultFormatter(Publisher): # 默認的被觀察者，發佈者，主持者

    def __init__(self, name):
        Publisher.__init__(self) # 調用發佈者的初始化函數
        self.name = name
        self._data = 0 # _ 表示該屬性不得被訪問，私有

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property # 將方法裝飾成屬性
    def data(self):
        return self._data

    @data.setter # 向被 property 裝飾成的屬性賦值時調用函數
    def data(self, new_value): # self.data = x 等價於 self.data(x)?
        try: # 嘗試
            self._data = int(new_value) # 將值轉化為int並傳遞給 self._data
        except ValueError as e: # 轉化失敗產生異常
            print('Error: {}'.format(e)) # 輸出
        else:
            self.notify() # 通知所有註冊的觀察者


class HexFormatter: # 十六進位的觀察者

    def notify(self, publisher): # 被通知時的行為
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name, hex(publisher.data)))


class BinaryFormatter: # 二進位的觀察者

    def notify(self, publisher): # 被通知時的行為
        print("{}: '{}' has now bin data = {}".format(type(self).__name__,
                                                      publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf) # 添加觀察者
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf) # 添加觀察者
    df.data = 21
    print(df)

    print()
    df.remove(hf) # 移除觀察者
    df.data = 40
    print(df)

    print()
    df.remove(hf) # 移除觀察者
    df.add(bf) # 添加觀察者
    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)

if __name__ == '__main__':
    main()

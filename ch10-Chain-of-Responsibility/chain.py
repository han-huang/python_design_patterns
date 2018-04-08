# coding: utf-8

class Event:

    def __init__(self, name): # 消息初始化
        self.name = name

    def __str__(self):
        return self.name # str(e) 得到消息


class Widget:

    def __init__(self, parent=None): # 初始化動態分發框架
        self.parent = parent # 責任鏈的上一級物件

    def handle(self, event): # 事件處理和分發和轉移
        handler = 'handle_{}'.format(event) # 事件處理函數的格式， 處理 x 事件的函數名稱為 handle_x
        if hasattr(self, handler): # 如果物件自己有該消息的處理函數
            method = getattr(self, handler) # 將自己的消息處理函數提取為 method
            method(event) # 執行處理函數，處理該消息，並消滅該消息(即處理完畢，不再傳播)
        elif self.parent: # 如果該物件在責任鏈上有上級物件
            self.parent.handle(event) # 將消息交給上級物件處理
        elif hasattr(self, 'handle_default'): # 如果該物件在責任鏈上無上級，且有預設處理函數
            self.handle_default(event) # 對事件調用預設處理函數
        # 若都沒有處理則忽略該消息，也可傳出異常？


class MainWindow(Widget):

    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):

    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):

    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)
    haha = SendDialog(msg)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)
        haha.handle(evt) # 由物件 haha 處理消息 'paint' 相當於 haha 截了 sd 的胡

if __name__ == '__main__':
    main()

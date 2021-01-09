

from tkinter import *
import random


class App:
    def __init__(self,master):
        # 创建矩形框
        frame = Frame(master)
        frame.pack()
        v = StringVar()
        #创建文本框
        self.e = Entry(frame,textvariable=v,bd='5')
        v.set('')
        self.v = v
        self.e.pack(padx=5)


        #创建两个按钮
        #按钮1  开始按钮，按下去执行'start_hi'
        self.button1 = Button(frame,text = 'start',fg='red',command=self.start_hi)
        self.button1.pack(side=LEFT)
        # 按钮2  开始按钮，按下去执行'start_stop'停止运行
        self.button2 = Button(frame,text='stop',fg = 'blue',command=self.say_stop)
        self.button2.pack(side=LEFT)
        self.root=master
        self.stop = 0

    #读取'yaojiang.txt'，获取抽奖名单
    def list_star(self):
        star = []
        file = open('yaojiang.txt','r+',encoding='utf-8')
        data = file.readlines()
        file.close()
        # 将抽奖名单里面信息读成一个数组，其中手机号4到8位变成XXXX
        for n in data:
            l1 = n.split(':')
            a = l1[0] + ':'+ l1[1][:4] + 'xxxx' + l1[1][8:12]
            a = a.strip()
            star.append(a)
        return star

   #开始“list_star”函数
    def start_hi(self):
        self.stop = 0
        #读取抽奖名单里面的信息
        star = self.list_star()
        self.update_clock(star)

    # 用来停止运行
    def say_stop(self):
        self.stop = 1   #stop=1 表示停止滚动
        # b = self.start()

    #开始随机抽奖
    def update_clock(self, star):
        # star表示抽奖名单
        b = random.choice(star) #从抽奖名单里面随机选一个
        self.v.set(b) #显示在文本框里面
        # 当按了停止按钮之后，退出出摇奖
        if self.stop == 1:
            return
        #每隔50ms，选一个人
        self.root.after(50, self.update_clock, star)


#初始化TK
root = Tk()

app = App(root)

#进入消息循环
root.mainloop()
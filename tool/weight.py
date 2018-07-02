#! --*-- coding: utf-8 --*--
__author__ = 'gaoxingsheng'

# 体重

import sys
from Tkinter import *


BMI_TABLE = [
    [18.5, "过轻"],
    [24, "正常"],
    [28, "过重"],
    [32, "肥胖"],
    [sys.maxint, "非常肥胖"],
]


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.result = StringVar()
        self.result.set("")
        self.pack()
        self.createWidgets()

    def fat_bmi(self, fat):
        for info in (BMI_TABLE):
            if fat < info[0]:
                return info[1]

        return "体脂率数据不正常"

    def boday_fat(self):
        print "hi there, everyone!"
        height = float(self.height_entry.get()) / 100
        weight = float(self.weight_entry.get())
        fat = weight / (height * height)
        self.result.set(self.fat_bmi(fat) + "%(fat).2f"%{'fat':fat})

    def createWidgets(self):
        label = Label(self, text = "身高")
        label.pack(fill=X, expand=1)

        self.height_entry = Entry(self, text = "输入身高")
        self.height_entry.pack(fill=X)

        label = Label(self, text = "体重")
        label.pack()

        self.weight_entry = Entry(self, text = "体重")
        self.weight_entry.pack(fill=X)

        self.QUIT = Button(self, text = "体脂率")
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.boday_fat
        self.QUIT.pack(fill=X)

        self.label_result = Label(self, textvariable = self.result)
        self.label_result.pack(fill=X)




root = Tk()
root.title = "体重"
root.geometry("300x300+300+0")
app = Application(master=root)
app.mainloop()
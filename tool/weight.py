#! --*-- coding: utf-8 --*--
from objc._objc import NULL

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

        return "数据不正常"

    def boday_fat(self, v1 = NULL, v2 = NULL):
        print "hi there, everyone!"
        try:
            height = float(self.height_entry.get()) / 100
            weight = float(self.weight_entry.get())
            height = max(height, 1)
            fat = weight / (height * height)
            self.result.set(self.fat_bmi(fat) + "%(fat).2f"%{'fat':fat})
        except Exception as e:
            self.result.set("无效数据")

    def createWidgets(self):
        font_normal = ('Helvetica', '22', 'bold')
        font_result = ('Helvetica', '40', 'bold')
        label = Label(self, text = "身高(cm)", font = font_normal)
        label.pack(fill=X, expand=1)

        var = StringVar()
        self.height_entry = Entry(self, text = "0", font = font_normal)
        self.height_entry['xscrollcommand'] = self.boday_fat
        self.height_entry.pack(fill=X)

        label = Label(self, text = "体重(kg)", font = font_normal)
        label.pack()

        self.weight_entry = Entry(self, text = "体重", font = font_normal)
        self.weight_entry['xscrollcommand'] = self.boday_fat
        self.weight_entry.pack(fill=X)

        btn_quit = Button(self, text = "体脂率", font = font_normal)
        btn_quit["fg"] = "red"
        btn_quit["command"] = self.boday_fat
        btn_quit.pack()
        self.btn_quit = btn_quit


        label = Label(self, text = "    ", font = font_normal)
        label.pack(fill=X)

        self.label_result = Label(self, textvariable = self.result, font = font_result)
        self.label_result.pack(fill=X)


root = Tk()
root.title = "体重"
root.geometry("500x300+500+0")
app = Application(master=root)
app.mainloop()
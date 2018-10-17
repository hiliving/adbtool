#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Frame

root = tkinter.Tk()
root.title("adb调试工具")
root.geometry('800x600')#是x 不是*
root.resizable(width=False, height=False)#宽不可变, 高可变,默认为True


a = Label(root, text="adb调试工具", bg="#fff", font=("Arial", 18), width=25, height=2)
a.pack(side=tkinter.TOP)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM


# 用于显示界面的文本
texts = tkinter.StringVar()
texts.set('当前未连接')

# Frame容器
frm = tkinter.Frame(root)
# 左侧面板
frm_L = Frame(frm)
# 右侧面板
frm_R = Frame(frm)

# 输入框
user=Entry()
pwd=Entry()
# 输入框对应文本

label_width=Label(frm_L, justify=tkinter.LEFT, text='窗体宽:',padx = 10,  bg='#fff', width=15, height=2).pack(side=tkinter.TOP)
label_height=Label(frm_L, justify=tkinter.LEFT,text='窗体高:',bg='#fff', width=15, height=2).pack(side=tkinter.TOP)
label_gravity=Label(frm_L, justify=tkinter.LEFT,text='对齐:',bg='#fff',padx = 10,  width=15, height=2).pack(side=tkinter.TOP)
label_marginx=Label(frm_L, justify=tkinter.LEFT,text='x偏移:',bg='#fff', width=15, height=2).pack(side=tkinter.TOP)
label_marginy=Label(frm_L, justify=tkinter.LEFT,text='y偏移:',bg='#fff', width=15, height=2).pack(side=tkinter.TOP)
label_msgtype=Label(frm_L, justify=tkinter.LEFT,text='物料类型:',bg='#fff', width=15, height=2).pack(side=tkinter.TOP)
label_jumptype=Label(frm_L,text='落地页类型:',bg='#fff', width=15, height=2).pack(side=tkinter.TOP)
label_adtype=Label(frm_L,text='是否广告:',bg='#fff', width=15, height=2)
label_blur=Label(frm_L,text='背景是否变暗:',bg='#fff', width=15, height=2)
label_showtime=Label(frm_L,text='定时关闭:',bg='#fff', width=15, height=2)
label_pageurl=Label(frm_L,text='物料地址:',bg='#fff', width=15, height=2)
label_jumpurl=Label(frm_L,text='落地页地址:',bg='#fff', width=15, height=2)
label_adid=Label(frm_L,text='内容id:',bg='#fff', width=15, height=2)



frm_L.pack(side=tkinter.LEFT)
frm.pack()


# 状态码
status = tkinter.IntVar()
status.set(1)
# 执行adb命令
def printhello():
    print(var.get())

    if status.get()==1:
        t["text"] = "连接成功"+var.get()
        t['fg'] = "#0ff"
        l['text'] = "断开"
        status.set(0)
    else:
        t["text"] = "当前未连接"
        t['fg'] = "#000"
        l['text'] = "连接"
        status.set(1)



t = Label(root, text=texts.get(),font=("Arial", 18), width=25, height=2)
t.pack()


l = Button(root, text="连接", command = printhello)
l.pack(side=tkinter.LEFT)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM


# 文本输入框
var = tkinter.StringVar()
e = tkinter.Entry(root, textvariable = var)
var.set("")
e.pack()




# 进入消息循环
root.mainloop()
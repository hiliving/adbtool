from tkinter import *
from tkinter.ttk import Combobox
import os

root=Tk()
root.title("快速安装工具")
root.geometry('800x600')#是x 不是*
root.resizable(width=False, height=False)#宽不可变, 高可变,默认为True

def d_sendMsg(*args):
    # 桌面的Tips
    os.system("adb shell am broadcast -a action_launcher_resume")
def d_playMsg(*args):
    # 桌面的Tips
    os.system("adb shell am broadcast -a action_launcher_resume")

btn=Button(text="桌面Tips广播", command = d_sendMsg)
btn.grid(row=13,column=6,rowspan=2,columnspan=2,padx=5, sticky=W,pady=15)
btn2=Button(text="互动Tips广播", command = d_playMsg)
btn2.grid(row=13,column=1,rowspan=2,columnspan=2,padx=5,sticky=W, pady=15)

root.mainloop()
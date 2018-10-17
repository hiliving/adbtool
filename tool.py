import datetime
import json
import time
from tkinter import *
from tkinter.ttk import Combobox
import os
import subprocess
root=Tk()
root.title("Tips调试工具")
root.geometry('800x600')#是x 不是*
root.resizable(width=False, height=False)#宽不可变, 高可变,默认为True


rowin = 2
colin = 2


var_adtype =StringVar()
var_width =StringVar()
var_height =StringVar()
var_marginx =StringVar()
var_gravity =StringVar()
var_marginy =StringVar()
var_msgtype =StringVar()
var_jumptype =StringVar()
var_blur =StringVar()
var_showtime =StringVar()
var_delaytime =StringVar()
var_pageurl =StringVar()
var_jumpurl =StringVar()
var_adid =StringVar()
var_title =StringVar()
var_ipinput =StringVar()
var_window_type =StringVar()
var_window_type.set(1001)
var_normal_msg = StringVar()

# 用于显示界面的文本
adbstatu = StringVar()
adbstatu.set('未连接')

v_adtype =0
v_msgtype =0
v_gravity=1010
v_jumptype =0
v_blur =StringVar().get()
v_delaytime =StringVar().get()
v_adid = 10202

label_width=Label(text='窗体宽:',bg='#fff',height=2)
label_height=Label(text='窗体高:',bg='#fff',height=2)
label_gravity=Label(text='对齐:',bg='#fff',height=2)
label_marginx=Label(text='x偏移:',bg='#fff',height=2)
label_marginy=Label(text='y偏移:',bg='#fff',height=2)
label_msgtype=Label(text='物料类型:',bg='#fff',height=2)
label_jumptype=Label(text='落地页类型:',bg='#fff',height=2)
label_adtype=Label(text='是否广告:',bg='#fff',height=2)
label_blur=Label(text='背景是否变暗:',bg='#fff',height=2)
label_showtime=Label(text='定时关闭:',bg='#fff',height=2)
label_pageurl=Label(text='物料地址:',bg='#fff',height=2)
label_jumpurl=Label(text='落地页地址:',bg='#fff',height=2)
label_adid=Label(text='内容id:',bg='#fff',height=2)
label_delaytime=Label(text='时间推移:',bg='#fff',height=2)
label_title=Label(text='标题:',bg='#fff',height=2)
label_adbstatu=Label(text='ADB:%s'%(adbstatu.get()),bg='#fff',height=2)
lable_windowType=Label(text='窗口类型:',bg='#fff',height=2)


width=Entry(root,width=10,bg="#c8f7fb", textvariable = var_width)
height=Entry(root,width=10,bg="#c8f7fb", textvariable = var_height)
gravity=Combobox(root, width=8,textvariable=var_gravity)
marginx=Entry(root,width=10,bg="#c8f7fb", textvariable = var_marginx)
marginy=Entry(root,width=10,bg="#c8f7fb", textvariable = var_marginy)
msgtype=Combobox(root,width=7,textvariable=var_msgtype)
jumptype=Combobox(root, width=7,textvariable=var_jumptype)
adtype=Combobox(root,width=7,textvariable=var_adtype)
blur=Combobox(root,width=7,textvariable=var_blur)
showtime=Entry(root,width=10,bg="#aaf1f7", textvariable = var_showtime)
delaytime=Entry(root,width=10,bg="#aaf1f7", textvariable = var_delaytime)
pageurl=Entry(root,width=60,bg="#c8f7fb", textvariable = var_pageurl)
jumpurl=Entry(root,width=60,bg="#c8f7fb", textvariable = var_jumpurl)
adid=Entry(root,width=10,bg="#c8f7fb", textvariable = var_adid)
title=Entry(root,width=60,bg="#c8f7fb", textvariable = var_title)
ipinput=Entry(root,width=16,bg="#c8f7fb", textvariable = var_ipinput)
windowType=Combobox(root,width=10, textvariable = var_window_type)
normal_msg_input=Entry(root,width=26,bg="#c8f7fb", textvariable = var_normal_msg)




# row,column,sticky
label_width.grid(row=3,column=1,sticky=E) #一个有sticky,一个没有sticky，以作区分
label_height.grid(row=4,column=1,sticky=E)
label_gravity.grid(row=5,column=1,sticky=E)
label_marginx.grid(row=6,column=1,sticky=E)
label_marginy.grid(row=7,column=1,sticky=E)
label_msgtype.grid(row=8,column=1,sticky=E)
label_jumptype.grid(row=3,column=3,sticky=E)
label_adtype.grid(row=4,column=3,sticky=E)
label_blur.grid(row=5,column=3,sticky=E)
label_showtime.grid(row=6,column=3,sticky=E)
label_adid.grid(row=7,column=3,sticky=E)
label_jumpurl.grid(row=9,column=1,sticky=E)
label_pageurl.grid(row=10,column=1,sticky=E)
label_title.grid(row=11,column=1,sticky=E)
label_delaytime.grid(row=8,column=3,sticky=E)
ipinput.grid(row=18,column=6,sticky=W)
label_adbstatu.grid(row=20,column=6,sticky=W,padx=6)
lable_windowType.grid(row =3,column=6,sticky=W,padx=31 )

# rowspan,columnspan
width.grid(row=3,column=2)
height.grid(row=4,column=2)
gravity.grid(row=5,column=2)
marginx.grid(row=6,column=2)
marginy.grid(row=7,column=2)
msgtype.grid(row=8,column=2)
jumptype.grid(row=3,column=4)
adtype.grid(row=4,column=4)
blur.grid(row=5,column=4)
showtime.grid(row=6,column=4)
adid.grid(row=7,column=4)
delaytime.grid(row=8,column=4)
jumpurl.grid(row=9,column=2,columnspan=5,sticky=E,padx=14)
pageurl.grid(row=10,column=2,columnspan=5,sticky=E,padx=14)
title.grid(row=11,column=2,columnspan=5,sticky=E,padx=14)
normal_msg_input.grid(row=15,column=6,pady=14)
windowType.grid(row=3,column=6,sticky=E,padx=14)


var_adid.set("可不填")
var_delaytime.set("互动Tips专用")
var_ipinput.set("")

def d_width():
    print(var_width.get())
def d_gravity(*args):
    print(gravity.get())
def d_adtype(*args):
    if adtype.get()=="是":
        v_adtype = 1
    else:
        v_adtype = 0
    print(adtype.get())
def d_jumptype(*args):
    if jumptype.get()=="图片":
        print("2")
    elif jumptype.get()=="activity":
        print("3")
    elif jumptype.get()=="网页":
        print("0")
    elif jumptype.get()=="APP下载":
        print("1")
    print(var_jumptype)

def d_isBlur(*args):
    if blur.get()=="是":
        print("1")
        var_blur.set("1")
    elif blur.get()=="否":
        print("0")
    print(var_blur)

def d_windowtype(*args):
    if blur.get()=="1001":
        print("1")
        var_window_type.set("1001")
    elif blur.get()=="1002":
        print("0")
        var_window_type.set("1002")
    print(var_blur)

def d_msgType(*args):
    # 0图片,1视频,2H5
    if var_msgtype.get()=="图片":
        print(" ")
    elif var_msgtype.get()=="视频":
        print(" ")
    elif var_msgtype.get()=="网页":
        print(" ")

def d_sendMsg(*args):

    if adtype.get()=="是":
        v_adtype = 1
    else:
        v_adtype = 0

    # 0图片,1视频,2H5
    if var_msgtype.get() == "图片":
        v_msgtype = 0
    elif var_msgtype.get() == "视频":
        v_msgtype = 1
    elif var_msgtype.get() == "网页":
        v_msgtype = 2


    if jumptype.get() == "图片":
        v_jumptype=2
    elif jumptype.get() == "activity":
        v_jumptype = 3
    elif jumptype.get() == "网页":
        v_jumptype = 0
    elif jumptype.get() == "APP下载":
        v_jumptype = 1

    if blur.get() == "是":
        v_blur = 1
    elif blur.get() == "否":
        v_blur = 0

    if gravity.get() == "居中1010":
        v_gravity = 1010
    elif gravity.get() == "左上1011":
        v_gravity = 1011
    elif gravity.get() == "右上1012":
        v_gravity = 1012
    elif gravity.get() == "左下1013":
        v_gravity = 1013
    elif gravity.get() == "右下1014":
        v_gravity = 1014


    if delaytime.get()=="互动Tips专用":
        v_delaytime = 10
    else:
        v_delaytime = delaytime.get()

    if adid.get()=="可不填":
        v_adid = 10202
    else:
        v_adid = adid.get()

    aa = 'adb shell am broadcast -a action_msg_test -e Gravity %s -e WIDTH %s -e HEIGHT %s -e PAGE_URL %s -e SHOW_TIME %s -e JUMP_URL %s -e JUMP_PAGE_TYPE %s -e MARGINX %s -e MARGINY %s -e TITLE %s -e ADTYPE %s -e BLUR_BG %s -e ADID %s  -e VIEW_TYPE %s -e TIME_DELAY %s' \
         %(str(v_gravity),
           str(var_width.get()),
           str(var_height.get()),
           str(pageurl.get()),
           str(var_showtime.get()),
           str(jumpurl.get()),
           str(v_jumptype),
           str(var_marginx.get()),
           str(var_marginy.get()),
           title.get(),
           str(v_adtype),
           str(v_blur),
           str(v_adid),
           str(var_window_type.get()),
           str(v_delaytime))

    # os.system(aa)
    print(aa)
    p = subprocess.Popen(aa, shell=FALSE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print('----',p.stdout.read())


def connectDevcie():
    '''检查设备是否连接成功，如果成功返回True，否则返回False'''
    try:
        '''获取设备列表信息，并用"\r\n"拆分'''
        # deviceInfo = subprocess.check_output('adb devices')
        deviceInfo= subprocess.Popen('adb devices', shell=FALSE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        '''如果没有链接设备或者设备读取失败，第二个元素为空'''
        b = str(deviceInfo.stdout.read()).split("\\r\\n")
        print(b[1].split("\\")[0])
        # print(b)
        label_adbstatu["text"] ="ADB已连接：%s"%(b[1].split("\\")[0])
        # print(deviceInfo)
    except Exception as e:
        print("Device Connect Fail:",e)

def d_getLauncherAd(*args):
    os.system("adb shell am broadcast -a action_launcher_resume")

def d_getVideoAd(*args):
    os.system("adb shell am broadcast -a ACTION_TO_REPEAT_REQUEST")

def d_resetFirst(*args):
    os.system("adb shell am broadcast -a action_test_reset_firsttime")

def d_netchanged(*args):
    os.system("adb shell am broadcast -a android_msg_test_moni_netchanged")

def d_screencut(*args):
    os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")

def d_getscreencut(*args):
    at = datetime.datetime.now().strftime('%H_%M_%S')
    os.system("adb pull /sdcard/screenshot.png d:/test/shot/ScreenShot_%s.png"%(str(at)))

def d_startapp(*args):
    # os.system("adb shell monkey -p com.bftv.fui.launcher -c android.intent.category.LAUNCHER 1")
    os.system("adb shell monkey -p com.bftv.fui.message -c android.intent.category.LAUNCHER 1")

def d_connadb(*args):
    cmd = "adb connect %s" % (var_ipinput.get())
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if "connect" in str(p.stdout.read()):
        connectDevcie()


def d_showkeep(*args):
    # os.system("adb shell am broadcast -a baofengtv.action.NO_OPERATION_START_APP")
    os.system("adb shell am broadcast -a baofengtv.screensaver.action.START")

btn=Button(text="全局Tips预览", command = d_sendMsg)
btn.grid(row=11,column=8,rowspan=2,padx=15, sticky=W,pady=1)


# 普通消息推送
def d_sendNormalMsg(*args):
    # 注意事项，python里不能直接把json转为字符串，需要用json.dumps进行转换，否则广播发不出去
    bb = "adb shell am broadcast -a bftv_broadcast_action_message -e taskid %s -e messageid %s -e message_json '%s' "%("125221","656545",json.dumps(var_normal_msg.get()))
    print('----', "adb shell am broadcast -a bftv_broadcast_action_message -e taskid %s -e messageid %s -e message_json %s"%("125221","656545",var_normal_msg.get()))
    os.system(bb)
    pass


btn=Button(text="普通消息推送", command = d_sendNormalMsg)
btn.grid(row=14,column=8,rowspan=2,padx=15, sticky=W,pady=1)

btn3=Button(text="请求桌面Tips", command = d_getLauncherAd)
btn3.grid(row=14,column=1,rowspan=2,padx=5, sticky=W, pady=15)

btn2=Button(text="请求互动Tips", command = d_getVideoAd)
btn2.grid(row=14,column=2,rowspan=2,padx=15,sticky=W, pady=5)

btn4=Button(text="重置初始状态", command = d_resetFirst)
btn4.grid(row=16,column=2,rowspan=2,padx=15,sticky=W, pady=15)

btn5=Button(text="模拟网络变化", command = d_netchanged)
btn5.grid(row=16,column=1,rowspan=2,padx=5,sticky=W, pady=5)

btn6=Button(text="显示屏保", command = d_showkeep)
btn6.grid(row=18,column=1,rowspan=2,padx=5,sticky=W, pady=5)

btn7=Button(text="连接adb", command = d_connadb)
btn7.grid(row=18,column=6,rowspan=2,padx=5,sticky=E, pady=1)

btn8=Button(text="截取屏幕", command = d_screencut)
btn8.grid(row=14,column=3,rowspan=2,padx=5,sticky=W, pady=1)


btn9=Button(text="获取截屏", command = d_getscreencut)
btn9.grid(row=16,column=3,rowspan=2,padx=5,sticky=W, pady=1)

btn10=Button(text="启动APP", command = d_startapp)
btn10.grid(row=16,column=4,rowspan=2,padx=5,sticky=W, pady=1)

gravity["values"] = ("居中1010", "左上1011", "右上1012","左下1013","右下1014")
gravity.current(0)
gravity.bind("<<ComboboxSelected>>", d_gravity)

adtype["values"] = ("是", "否")
adtype.current(0)
adtype.bind("<<ComboboxSelected>>", d_adtype)

jumptype["values"] = ("图片", "activity", "APP下载", "网页")
jumptype.current(0)
jumptype.bind("<<ComboboxSelected>>", d_jumptype)

blur["values"] = ("是", "否")
blur.current(0)
blur.bind("<<ComboboxSelected>>", d_isBlur)

windowType["values"] = ("1001", "1002")
blur.current(0)
blur.bind("<<ComboboxSelected>>", d_windowtype)

msgtype["values"] = ("图片", "视频","网页")
msgtype.current(0)
msgtype.bind("<<ComboboxSelected>>", d_msgType)




check=Label(text="")
check.grid(row=1,column=0,padx=45,pady = 10)
titleLable=Label(text="", font=("Arial", 11))
titleLable.grid(row=1,column=3,pady = 10)

connectDevcie()

print (datetime.datetime.now().strftime('%H_%M_%S'))


root.mainloop()
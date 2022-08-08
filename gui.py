from tkinter import *

import models


def model_contents():
    dic = {0: '自动开时间宝箱', 1: '自动探索'}
    s = "已结束" + dic.get(var.get()) + "项"
    lb.config(text=s)
    if var.get()==0:
        models.open_1()
    if var.get()==1:
        models.auto_expore()

root = Tk()
root.title('蜗牛自动化辅助')
root.geometry('500x150')

#单选


var = IntVar()
rd1 = Radiobutton(root,text="自动开宝箱",variable=var,value=0,command=None)
rd1.pack()

var = IntVar()
rd1 = Radiobutton(root,text="自动探索(需要先手动把正在进行的探索结束掉)",variable=var,value=1,command=None)
rd1.pack()


btn1 = Button(root, text='开始执行', command=model_contents)
btn1.pack()
#btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

lb = Label(root)#贴个空的，以后需要显现就赋值
lb.pack()

root.mainloop()


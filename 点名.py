# -*- coding: utf-8 -*-
# @Time    : 18-12-30 下午6:38
# @Author  : Felix Wang


from tkinter import *
import tkinter.font as tkFont
import time
import random
import gc
import os, sys
import chardet


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


def a():
    lb.delete(0, END)


def get_names():
    names = []
    name_path = os.path.join(BASE_DIR, 'name.txt')
    with open(name_path, 'rb') as f:
        data = f.read()
        cod = chardet.detect(data)['encoding']
        for name in data.decode(cod).strip().split('\n'):
            if name.strip():
                names.append(name.strip())
        return names


def name():
    pict["image"] = huang_gif
    button["text"] = '先别点我'
    do = len(names) - 1
    ft1 = tkFont.Font(family='Fixdsys', size=80, weight=tkFont.BOLD)
    hua = time.time()
    random.shuffle(names)

    a = list(range(0, do))
    random.shuffle(a)
    use = a[0:int(v.get())]
    ren = int(v.get())
    for i in range(ren):
        for a in range(23):
            index = random.randint(0, do)
            echo["text"] = names[index]
            root.update_idletasks()
            time.sleep(1 / 23 - 0.003)
        pict['image'] = huaji_gif
        echo["text"] = names[use[i]]
        lb.insert(END, names[use[i]])
        root.update_idletasks()
        for a in range(5):
            root.update
            time.sleep(0.06)
        pict['image'] = huang_gif
    button["text"] = '开始点名'
    for x in locals().keys():
        del locals()[x]
    gc.collect()
    pict['image'] = huaji_gif
    scrolly.update


try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    names = get_names()

    root = Tk()

    root.title("随机点名器(by 王以涛)")

    center_window(root, 570, 160)

    ft = tkFont.Font(family='Fixdsys', size=40, weight=tkFont.BOLD)
    ft1 = tkFont.Font(family='Fixdsys', size=80, weight=tkFont.BOLD)
    echo = Label(root, text='我叫雷锋', font=ft, width=8)
    echo.grid(row=1, column=1, columnspan=2)

    scrolly = Scrollbar(root)
    scrolly.grid(row=1, column=5, rowspan=2, ipady=30)
    lb = Listbox(root, yscrollcommand=scrolly.set, exportselection=False, height=6)
    lb.grid(row=1, column=3, rowspan=2, columnspan=2, pady=0)
    scrolly['command'] = lb.yview

    button = Button(root, text='删除所选名字', command=lambda x=lb: x.delete(ACTIVE))
    button.grid(row=3, column=3)
    button = Button(root, text='删除所有名字', command=a)
    button.grid(row=3, column=4)

    v = StringVar()
    Scale(root, from_=1, to=len(names), resolution=1, orient=HORIZONTAL, variable=v).grid(row=2, column=1)

    data_dir = os.path.join(BASE_DIR, "img")
    huaji_gif = PhotoImage(file=resource_path(os.path.join(data_dir, 'huaji.gif')))
    huang_gif = PhotoImage(file=resource_path(os.path.join(data_dir, 'huang.gif')))
    pict = Label(root, image=huaji_gif)
    pict.grid(row=1, column=0, rowspan=3)
    button = Button(root, text='开始点名', command=name)
    button.grid(row=2, column=2)

    root.mainloop()
except Exception as e:
    print('错误信息', e)
    time.sleep(60)

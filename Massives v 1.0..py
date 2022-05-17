# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox
import math

window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('500x350')

lbl1 = Label(window, text="Введите строку 1:", font=("Time New Roman", 14))
lbl1.place(x=1, y=1)

txt1 = Entry(window, width=50)
txt1.place(x=170, y=6)

lbl1 = Label(window, text="Введите строку 2:", font=("Time New Roman", 14))
lbl1.place(x=1, y=30)

txt2 = Entry(window, width=50)
txt2.place(x=170, y=36)

txt = scrolledtext.ScrolledText(window, width=40, height=10)  
txt.place(x=5, y=95)

lbl3 = Label(text="Результат", font=("Time New Roman", 16))
lbl3.place(x=116, y=65)

def clicked():
    txt = scrolledtext.ScrolledText(window, width=40, height=10)  
    txt.place(x=5, y=95)
    num1 = list(txt1.get())
    num2 = list(txt2.get())
    num3 = num1
    num4=list(filter(lambda x:x in num1, num2))
    num3=num3+num4
    txt.insert(INSERT,num3)

btn = Button(window, text="Сгенерировать!", command=clicked)  
btn.place(x=370, y=155)  
window.mainloop()





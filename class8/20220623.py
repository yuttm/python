from dis import dis
from time import time
from tkinter import *


def nofun():
    global sw
    print("aaaaaaaaa")
    if sw:
        display.config(text=int(entry_data.get()) * 2.54)
    else:
        display.config(text=0)
    sw = not (sw)


def goodfun():
    display.config(text=int(entry_data.get()))


win = Tk()
win.title('金子豪比我慢')
sw = True

bty = Button(win, text="請輸入公分", command=goodfun)
bty.pack()

entry_data = Entry(win)
entry_data.pack()

btn = Button(win, text="click me", command=nofun)
btn.pack()

display = Label(win, text="2.54", fg='#C900FF', bg="#C9FFE2")
display.pack()

sw = True

win.mainloop()
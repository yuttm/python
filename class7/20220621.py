from time import time
from tkinter import *

win = Tk()
win.title('廖子豪比我慢')


def nofun():
    global sw
    print("aaaaaaaaa")
    if sw:
        display.config(text="hi", fg="blue", bg="#CC5D7B")
    else:
        display.config(text="oh", fg='#C900FF', bg="#C9FFE2")
    sw = not (sw)


btn = Button(win, text="click me", command=nofun)
btn.pack()

sw = True

display = Label(win, text="oh", fg='#C900FF', bg="#C9FFE2")
display.pack()

win.mainloop()

#display顯示物件
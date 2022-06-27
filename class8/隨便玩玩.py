from tkinter import *


def nofun():
    if b.get() == "+":
        display4.config(text=int(a.get()) + int(c.get()))
        ans = int(a.get()) + int(c.get())
    elif b.get() == "-":
        display4.config(text=int(a.get()) - int(c.get()))
        ans = int(a.get()) - int(c.get())
    elif b.get() == "*":
        display4.config(text=int(a.get()) * int(c.get()))
        ans = int(a.get()) * int(c.get())
    elif b.get() == "/":
        display4.config(text=int(a.get()) / int(c.get()))
        ans = int(a.get()) / int(c.get())
    display5.config(text="位元數=" + str(len(str(ans))))


win = Tk()
win.title('hi')
display1 = Label(win, text="輸入文字")
display1.pack()

a = Entry(win)
a.pack()

display2 = Label(win, text="輸入符號")
display2.pack()

b = Entry(win)
b.pack()

display3 = Label(win, text="輸入數字")
display3.pack()

c = Entry(win)
c.pack()

btn = Button(win, text="結果", command=nofun)
btn.pack()

display4 = Label(win, text="")
display4.pack()

display5 = Label(win, text="位元數")
display5.pack()

win.mainloop()
from tkinter import *


def yu_juice():
    global juice
    for i in juice:
        if i == entry.get():
            # print("此果汁重複")
            display4.config(text="此果汁重複")
            break
    else:
        juice.append(entry.get())
        t = ""
        for i in juice:
            t += i + '\n'
        display4.config(text=t)


def ttm_juice():
    global juice
    t = ""
    for i in juice:
        t += i + '\n'
    display4.config(text=t)


def remove_juice():
    global juice
    if entry.get() in juice:
        juice.remove(entry.get())
        t = ""
        for i in juice:
            t += i + '\n'
        display4.config(text=t)
    else:
        display4.config(text + "已不存在")


juice = []
win = Tk()
win.title('hi')
display1 = Button(win, text="輸入菜單", command=yu_juice)
display1.grid(row=0, column=0)

display2 = Button(win, text="輸入顯示菜單", command=ttm_juice)
display2.grid(row=1, column=0)

display3 = Button(win, text="移除")
display3.grid(row=2, column=0)

# btn = Button(win, text="結果", command=nofun)
# btn.grid(row=2, column=2)

display4 = Label(win, text="test")
display4.grid(row=0, rowspan=2, column=1)

entry = Entry(win)
entry.grid(row=2, column=1)

# display5 = Label(win, text="位元數")
# display5.grid()

win.mainloop()

# while True:
#     print("1輸入想要的果汁\2顯示目前的果汁\3離開系統")
#     x = input("輸入功能變換")
#     if x == "1":
#         yu_juice(juice)
#         j = int(input("輸入想要的果汁"))
#         for i in juice:
#             if i == j:
#                 print("此果汁重複")
#                 break
#         else:
#             juice.append(j)
#     elif x == "2":
#         ttm_juice(juice)
#         # print(juice)
#     elif x == "3":
#         break
#     else:
#         print("查無東西")
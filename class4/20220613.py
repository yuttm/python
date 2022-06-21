# import turtle

# turtle.shape("turtle")
# turtle.pensize(40)
# turtle.pencolor("pink")
# for i in range(5):
#     # turtle.stamp()
#     # turtle.penup()
#     # turtle.forward(50)
#     turtle.right(144)
#     turtle.forward(100)
# turtle.done()

# i = 0
# x = int(input("輸入數字:"))
# A = 0
# while i <= x:
#     A +=  i
#     i += 1
#     print(i)

# print(A)

# while True:
#     print("1頻果汁\n2柳橙汁\n3葡萄汁\n4離開系統")
#     ans = input("請輸入")
#     if ans == "1":
#         print("頻果汁")
#     elif ans == "2":
#         print('柳橙汁')
#     elif ans == "3":
#         print("葡萄汁")
#     elif ans == "4":
#         break
#     else:
#         print("erro")
import random

# random.randrange(停止值)
# random.randrange(起始值,終止值,遞進值)
# print(random.randrange(3))
# print(random.randrange(0, 10, 2))
# print(random.randint(1, 3))
num = random.randint(1, 100)
times = 3
while True:
    ans = int(input("請輸入:"))
    times -= 1
    if times == 0:
        print("end")
        break
    if ans < num:
        print("太小了")
    elif ans > num:
        print("太大了")
    elif ans == num:
        print("correct")
        break
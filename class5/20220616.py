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

drink = ["頻果汁", "柳橙汁", "葡萄汁", "離開系統"]
while True:
    print("1頻果汁\n2柳橙汁\n3葡萄汁\n4離開系統")
    ans = int(input("請輸入"))
    if ans == 4:
        break
    elif ans > len(drink):
        print('error')
    else:
        print(drink[ans - 1])

    drink[1] = "柳橙汁"
    drink[2] = "葡萄汁"
    drink[3]

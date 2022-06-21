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

# drink = ["頻果汁", "柳橙汁", "葡萄汁", "離開系統"]
# while True:
#     print("1頻果汁\n2柳橙汁\n3葡萄汁\n4離開系統")
#     ans = int(input("請輸入"))
#     if ans == 4:
#         break
#     elif ans > len(drink):
#         print('error')
#     else:
#         print(drink[ans - 1])
#append新增元素到字串最後
#insert在指定位置插入指定元素
#pop()移除串列裡的最最後一個
#sort由小至大排序串列元素
#reverse顛倒串列順序
#l[1,2,3,]
#index+l.index("1")

juice = []
while True:
    print("1輸入想要的果汁\2顯示目前的果汁\3離開系統")
    x = input("輸入功能變換")
    if x == "1":
        j = int(input("輸入想要的果汁"))
        for i in juice:
            if i == j:
                print("此果汁重複")
                break
        else:
            juice.append(j)
    elif x == "2":
        print(juice)
    elif x == "3":
        break
    else:
        print("查無東西")

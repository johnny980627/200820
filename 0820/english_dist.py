d = {}
print("歡迎來到英文高手系統")
while True:
    print("1.建立字典")
    print("2.列出所有單字")
    print("3.英翻中")
    print("4.中翻英")
    print("5.測驗")
    print("6.離開")
    option = int(input("請輸入選項:"))
    if option ==  6:
        break
    elif option == 1:
        while True:
            voc = input('請輸入新英文單字:')
            if voc == "0":
                break
            if voc not in d:
                voc_ch = input('請輸入中文:')
                d[voc] = voc_ch
            else:
                print("已存在!")
    elif option== 2:
        s = sorted(d)
        print(s) 
        for i in s:
            print(i, ":", d[i])
    elif option== 3:
        while True:
            voc = input("請輸入英文單字(按0離開):")
            if voc == "0":
                break
            if voc in d:
                print(voc,"的中文是",d[voc])
            else:
                print("字典裡沒有這個單字")
    elif option== 4:
        while True:
            got = False
            voc_ch = input("請輸入中文(按0離開):")
            if voc_ch == "0":
                break
            for k,v in d.items:
                if voc_ch == v:
                    print(voc_ch,"的英文是", k )    
                    got = True
            if not got:
                print("字典裡沒有這個單字")
    elif option== 5:
        score = 0
        for k,v in d.items():
            print(v)
            ans = input(":") 
            if ans == k:
                score = score + 1
                print("答對!")
            else:
                print("答錯!")
        print("總分為",score,"分")


            
            
            
            
            





















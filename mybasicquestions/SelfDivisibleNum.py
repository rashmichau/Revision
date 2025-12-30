# input: 36
# output :3 True
#         6 True

num= input("enter any num : ")
for i in num:
    try:
        if int(num)%int(i)==0:
            print(i,"True")
        else:
            print("num is not self devesible",i)
    except ZeroDivisionError:
        print("zero is not divisible")
        

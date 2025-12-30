lis =[1,2,3,4,2,6]
num=int(input("enter any num : "))
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]+lis[j]==num:
            print(lis[i],lis[j])
        
            
        

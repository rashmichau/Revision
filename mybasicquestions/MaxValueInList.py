# Maximun occurance of value in Given List
input : [1,1,1,3,4,5]
# output : 3
lis=[1,2,3,4,4,32,5,5]
dic={}
max=0
for i in lis:
    if i not in (dic):
        dic[i]=1
    
    elif i in (dic):
        dic[i]+=1
print(dic)
for key,value in dic.items():
    
    if value >max:
        max=value
print(max)

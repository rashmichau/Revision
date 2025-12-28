# Count number of matching characters in a pair of string
# input1 : raam , input2 : shyam
# output : 1
s1 = input("enter any string : ")
s2 = input("enter any string : ")
count=0
for i in s2:
    if i in s1:
        print(i)
        count+=1
print(count)
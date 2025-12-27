# Accept strings containing all vowels
# nput: "education"
# Output: True
# s = input("enter any string : ")
# v="aeiouAEIOU"
# count=0
# for i in s:
#     if i in v:
#         print(i)
#         count+=1
# print(count)




s = "education"
v = 'aeiou' 
a = set() 
for char in s.lower():
    if char in v: 
        a.add(char)  
    if len(a) == 5:  
        print("True")
        break
else:
    print("False")
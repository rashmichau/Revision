# Avoid Spaces in string length
#ex: input: "rashmi chaudhary"
#output: 15
s1=input("enter string : ")
print(len(s1))
sum=""
for i in s1:
    if i==" ":
        continue
    sum+=i
print(sum)
print(len(sum))
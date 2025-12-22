# Reverse words in a String
s= input("enter string : ")
print(s[ : :-1])

# another method
result=""
for i in s:
    result=i+result
print(result)

# Remove Letters From a Stringe
s=s.replace(s[2]," ")
print(s)

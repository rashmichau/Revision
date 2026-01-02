# For removing ith character from a string
# input = "PythonPrograming",i:6
# output=Pythonrograming

s = input("Enter any string : ")
l=int(input("enter any num : "))
s2=""
for k in range(len(s)):
    if k==l:
        continue
    s2+=s[k]
print(s2)

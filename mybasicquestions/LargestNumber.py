# Write a Python program to find the largest of three numbers.
x=input("enter  num : ")
y=input("enter  num :")
z=input("enter num :")
if x>y and x>z:
    print("largest number is",x)
elif y>z:
    print("largest num is ",y)
elif x==y==z:
    print("all nums are equal")
else:
    print("largest num is ",z)
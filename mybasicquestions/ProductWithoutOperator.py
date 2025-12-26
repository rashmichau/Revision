# Write a Python program to find the product of two numbers without using the * operator
x =int(input("enter num : "))
y=int(input("enter second num : "))
prod=0
for i in range(1,x+1):
    prod+=y
print(prod)
# Write a Python program to check if a number is a perfect square.
num =int(input("enter a num :"))
for i in range(1,num+1):
    square=i*i
    if num==square:
        print("number is perfect square of",i)
        break
else:
    print("num is not perfect square ")


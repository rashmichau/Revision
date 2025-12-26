#  Write a Python program to calculate the power of a number using loops.
num=int(input("Enter any num : "))
pow=int(input("Choose poewr : "))
result=1
for i in range(pow):
    result*=num
print(result)


#  Write a Python program to calculate the power of a number using loops.
# input : x=3 , pow=2
# output : 9
num=int(input("Enter any num : "))
pow=int(input("Choose poewr : "))
result=1
for i in range(pow):
    result*=num
print(result)


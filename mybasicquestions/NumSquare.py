# Write a Python program to find the square of a number without using multiplication.

# num = int(input("enter any num : "))
# square=0
# for i in range(abs(num)):
#     square+=num
# print(square)

# Write a Python program to convert a decimal number to binary.
num=int(input("enter  num : "))
# print(bin(num)[2:])

# one more method
binary=""
if num==0:
    print("binary num is 0")
else:
    while num>0:
        reminder=num%2
        binary=str(reminder)+binary
        num=num//2
    print(binary)

# Factorial of any num
# input : 3
# output :6
num =int(input("enter any num : "))
fact=1
for i in range(num,0,-1):
    fact*=i
    print(i)
print(fact)

# maximum of three arrays
a=[1,8,9,5]
b=[2,7,9,8]
c=[3,9,77,6]
# a.extend(c)
# a.extend(b)
# print(max(a))

# second method
x=max(a)
y=max(b)
z=max(c)
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
else:
    print(z)
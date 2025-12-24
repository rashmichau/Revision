# Uppercase Half String
s=input("enter any string :")
if len(s)%2==0:
    a=len(s)/2
    s1=s[:int(a)]
    s2=s[int(a):]
    s3=s1.upper()
    print(s3+s2)
else:
    print("string  is not in equal parts")




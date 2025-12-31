# Least Frequent Character
# Maximum frequency character
s = input("enter any str : ")
d ={}
l=[]

for i in s:
    if i  in d:
        d[i]+=1
    else:
        d[i]=1
print(d) 
for k,v in d.items():
    l.append(v)
print(min(l))
print(max(l))



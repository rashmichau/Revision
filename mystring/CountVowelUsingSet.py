# Count number of vowels using sets
s = input("enter any string : ")
v ="aeiouAEIOU"
s2 = set()
count=0
for i in s:
    if i in v:
        s2.add(i)
        count+=1
print(s2)
print(count)
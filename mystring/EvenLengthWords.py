# Print even-length words in string
s = input("enter a sentence")
w=s.split()
s1=[]
for i  in w:
    if len(i)%2==0:
        s1.append(i)
w=" ".join(s1)
print(w)

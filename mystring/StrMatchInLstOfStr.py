# Find all close matches of input string from a list
l = ["book","read","match","python","looks","advanced"]
s=input("enter any string : ")
for i in l:
    if i==s:
        print("matches input string")
        break
else:
    print("string not matches from list string ")
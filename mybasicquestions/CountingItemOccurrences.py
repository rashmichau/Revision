# Count Item Occurrences from the list of items
# input:[a,d,g,u,i,a,d,r,c]
#       item:a
# output:2

l = ["book","shop","computer","python","language","python","book","salt","rust"]
item = input("Enter somthing from lst : ")
count=0
for i in l:
    if i==item:
        count+=1
        

print(count)
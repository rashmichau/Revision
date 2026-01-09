# Sort a List In Descendeing Order
l =[4,5,6,3,8,9,2,1,1]

# method 1
# l.sort(reverse=True)
# print(l)


# Method 2
sortedlst=[]
while l:
    minimum=l[0]
    for i in l:
        if i < minimum:
            minimum=i
    sortedlst.append(minimum)
    l.remove(minimum)
sortedlst.reverse()
print(sortedlst)



# Flatten A Nested List
# input:[[1,2],[3,4]]
# output:[1,2,3,4]

l = [[1,2,3],[4,5,6]]
l2=[]
for i in l:
    for j in i:
        l2.append(j)
print(l2)
    
        
import copy
original = [[1,2,3],[4,5,6]]
shallow = copy.copy(original)
shallow[0][0]=5
print(shallow)
print(original)

deep = copy.deepcopy(original)
deep[1][0]=5
print(deep)
print(original)
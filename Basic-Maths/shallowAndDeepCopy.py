import copy

a = [1,2,3,4,5,6]

b = a

b[0] = 0

print(a)
print(b)


original = [[1, 2, 3], [4, 5, 6]]
shallow_copied = copy.copy(original)
deep_copied = copy.deepcopy(original)


shallow_copied[0][1] = 4
deep_copied[0][0] = 8


print(original)
print(shallow_copied)
print(deep_copied)
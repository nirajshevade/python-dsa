import copy

arr = [1,1,9,2,3,4]
arr.extend([40,50,60,70])
arr.remove(1)
print(arr)
arr2 = arr.copy()
arr2.pop()
print(arr)
print(arr2)
print(sorted(arr2))
print(f"Sum: {sum(arr)} | Max: {max(arr)} | Min: {min(arr)} | Length: {len(arr)}")

print(all(arr))

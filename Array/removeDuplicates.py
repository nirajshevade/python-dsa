# Using Set method
def removeDuplicatesBySet(arr):
    seen = set()
    
    index = 0
    
    for num in arr:
        if num not in seen:
            seen.add(num)

            arr[index] = num
            
            index += 1
    
    return index

# Using 2 pointer method
def removeDuplicatesByTwoPointers(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

arr1 = [0,1,1,1,2,2,2,3,3,4,4,5]
arr2 = [0,0,0,1,1,1,2,2,2,2,3,3,4,4,5,5,5,5,6,6,6,7,7,8,9,9,9,9,9,9]
k = removeDuplicatesBySet(arr1)
print(k)
print(arr1[:k])

x = removeDuplicatesByTwoPointers(arr2)
print(x)
print(arr2[:x])
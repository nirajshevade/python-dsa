def first_occurence(arr, size, i , val):
    if i == size:
        return -1
    if arr[i] == val:
        return i    
    return first_occurence(arr, size, i+1, val)

arr = []
n = int(input("Enter Number of elements: "))

for k in range(n):
    arr.append(int(input(f"Enter value {k}: ")))

size = len(arr)

val = int(input("Enter the value to be find: "))

index = first_occurence(arr, size, 0, val)

if index!= -1:
    print(f"The value {val} is found at index {index}.")
else:
    print(f"The value is not in Array.")

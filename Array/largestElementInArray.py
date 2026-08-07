def largest(arr, n):
    le = arr[0]
    for i in range(1 , n):
        if arr[i] > le:
            le = arr[i]  
    return le



n = int(input("Enter Array Size: "))
arr = []
for i in range(0, n):
    arr.append(int(input("Enter Element in Array: ")))

print("Array: ", arr)
print("Largest Element: ", largest(arr, n))
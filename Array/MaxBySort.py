def display(arr):
    return f"Array: {arr}"


def selectionSort(arr, size):
    for i in range(0, size-1):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp
            
            
            
arr = []
size = int(input("Enter Size: "))

for i in range(0, size):
    arr.append(int(input(f"Enter element {i+1}: ")))

print(display(arr))

selectionSort(arr, size)

print(f"Array After Sorting: {display(arr)}")

print(f"Max Element in Array: {arr[size-1]}")


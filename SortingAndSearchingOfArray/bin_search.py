def disp_array(arr):

    print(f"Array is: ")

    for i in arr:
        print(i)


def bin_search(arr, size, val):
    
    left = 0
    right = size - 1

    while left <= right:
        mid = (left + right)//2

        if val > arr[mid]: left = mid + 1
        elif val < arr[mid]: right = mid - 1
        else: return mid
    return -1

size = int(input("Enter Length of Array: "))

arr = []
print("Enter Elements of Array: ")
for i in range (0, size):
    arr.append(int(input(f"Enter element {i+1}: ")))



disp_array(arr)

val = int(input("Enter Value to be search: "))

result = bin_search(arr, size, val)

if result == -1: print("Not Found")
else: print(f"Found at {result} index")


def disp_array(arr):

    print(f"Array is: ")

    for i in arr:
        print(i)


def lin_search(arr, size, val):
    
    for i in range(0, size):
        
        if arr[i] == val:
            return i
    return -1


size = int(input("Enter Length of Array: "))

arr = []
print("Enter Elements of Array: ")
for i in range (0, size):
    arr.append(int(input(f"Enter element {i+1}: ")))



disp_array(arr)

val = int(input("Enter Value to be search: "))

result = lin_search(arr, size, val)

if result == -1: print("Not Found")
else: print(f"Found at {result} index")


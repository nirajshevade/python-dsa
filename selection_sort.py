def disp_array(arr):

    print(f"Array is: {arr}")



def selection_sort(arr, size):
    for i in range(0, size):
        
        min_index = i

        for j in range(i+1, size):
            if(arr[j] < arr[min_index]):
                min_index = j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp



size = int(input("Enter Length of Array: "))

arr = []
print("Enter Elements of Array: ")
for i in range (0, size):
    arr.append(int(input(f"Enter element {i+1}: ")))



disp_array(arr)

selection_sort(arr, size)

print(f"The Array after selection sort: {arr}")



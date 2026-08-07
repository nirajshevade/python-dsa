def disp_array(arr):

    print(f"Array is: {arr}")



def bubble_sort(arr, size):

    for i in range(1, size):

        for j in range(0, size-i):

            if (arr[j] > arr[j+1]):

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

size = int(input("Enter Length of Array: "))

arr = []
print("Enter Elements of Array: ")
for i in range (0, size):

    arr.append(int(input(f"Enter element {i+1}: ")))



disp_array(arr)

bubble_sort(arr, size)

print(f"The Array after bubble sort: {arr}")



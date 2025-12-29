
def display(arr):
    print("The original Array is: {}".format(arr))

def insertion_sort(arr, size):
    for i in range(1, size):
        
        j = i - 1
        
        while (j >= 0):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                break
            j = j - 1

arr = []

size = int(input("Enter the size of Array: "))

for i in range(0, size):
    arr.append(int(input("Enter array element {}: ".format(i+1))))

display(arr)
insertion_sort(arr, size)

print("The Array after Insertion sort: {}".format(arr))


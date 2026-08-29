def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
        
    arr[-1] = temp
    return arr


arr = [1,2,3,4,5]
print(arr)
n = len(arr)
print(leftRotateByOne(arr, n))


          
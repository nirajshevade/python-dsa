def checkIfSorted(arr, n):
    for i in range(0, n):
        for j in range(i+1,n):
            if arr[j] < arr[i]:
                return False
    return True

n = int(input())
arr= []
for i in range(0,n):
    arr.append(int(input()))

print(checkIfSorted(arr, n))
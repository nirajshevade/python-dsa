def reverseArraay(arr):
    size = len(arr)
    ans = [0] * size

    for i in range(0, n):
        ans[i] = arr[size - i - 1]

    return ans

n = int(input("Enter size: "))
arr = [0] * n
for i in range(0, n):
    arr[i] = int(input(f"Enter element {i}: "))


print("Array: ", arr)

result = reverseArraay(arr)
print("Reversed Array: ",result)
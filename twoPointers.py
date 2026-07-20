def reverseArray(arr):
    p1 = 0

    p2 = len(arr) - 1

    while p1 < p2:

        arr[p1], arr[p2] = arr[p2], arr[p1]

        p1 += 1

        p2 -= 1

arr = [12, 23, 34, 45, 56, 67]
reverseArray(arr)

print(" ".join(map(str, arr)))
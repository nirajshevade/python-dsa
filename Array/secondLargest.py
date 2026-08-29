def secondLargestElement(arr, n):
    if n < 2:
        return -1, -1

        
    se = sse = float('inf')
    le = sle = float('-inf')
    
    for num in arr:
        if num < se:
            sse = se
            se = num
        elif se < num < sse:
            sse = num
            
        if num > le:
            sle = le
            le = num
        elif le < num < sle:
            sle = num
    
    
    if sse == float('inf') or sle == float('-inf'):
        return -1, -1
    
    return sse, sle

arr = []

n = int(input())
for i in range(n):
    arr.append(int(input()))


sse, sle = secondLargestElement(arr, n)

print("========")
print(sse," | ", sle)
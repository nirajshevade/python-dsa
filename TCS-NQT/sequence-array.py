n = int(input())

arr = list(map(int, input().split()))

print(arr)
MAX = 100000
freq = [0] * (MAX + 1)

for x in arr:
    freq[x] += 1

answer = 0

for x in range(1, MAX + 1):
    if freq[x] == 0:
        continue
    
    for y in range(1, freq[x] + 1):
        if freq[y] >= x:
            answer += 1
            
            
print(answer)
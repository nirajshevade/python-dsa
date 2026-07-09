import math

def print_divisors(num):
    arr = []
    for i in range(1, math.isqrt(num)+1):
        if(num%i == 0):
            arr.append(i)

            if i != num // i:
                arr.append(num // i) 

    return sorted(arr)

num = int(input("Enter a number: "))
result = print_divisors(num)
print(f"All divisors of {num}: {result}")

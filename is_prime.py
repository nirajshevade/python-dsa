import math

def is_prime(num):
    count = 0
    for i in range(1, math.isqrt(num)+1):
        if(num % i == 0):
            count += 1
            if(num // i != i):
                count += 1
    return count == 2
    
num = int(input("Enter a number: "))
print(is_prime(num))
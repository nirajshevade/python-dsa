import math
import time

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def print_k_primes(k):
    count = 0
    num = 2

    while count < k:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

def sum_k_primes(k):
    count = 0
    num = 2
    total = 0

    while count<k:
        if is_prime(num):
            total += num
            count += 1
        num += 1
    
    print("\n")
    
    # prints Hurray only if total is a perfect square
    root = math.isqrt(total)
    if (root ** 2 == total):
        print("Hurray!!")
    return total


start_time = time.time()
k = int(input("Input Limit: "))
print(f"First {k} prime numbers are:")
print_k_primes(k)

print(end="")
print(f"\nSum of first {k} prime numbers is: {sum_k_primes(k)}")

end_time = time.time()

print(f"Execution Time: {end_time - start_time:.6f} seconds")
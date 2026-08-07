def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

num = int(input("Enter a number: "))
for i in range(0, num):
    print(fibonacci(i), end=" ")   
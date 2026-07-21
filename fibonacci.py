#using recursion

def fibonacci(num):
    if num <= 1:
        return num
    last = fibonacci(num-1)
    slast = fibonacci(num-2)
    
    return last + slast

num = int(input("Enter a number: "))
print(fibonacci(num))
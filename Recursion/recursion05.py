# def fact(num):
#     if num == 0:
#         return 1
#     return num * fact(num-1)


def fact(num):
    if num > 0:
        return num * fact(num-1)
    else: return 1

num = int(input("Enter a number: "))
print(f"Factorial of {num}:", fact(num))
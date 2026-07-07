def digit_count(num):
    digit = 0

    while(num > 0):
        num //= 10
        digit += 1

    return digit


num = int(input("Enter a number: "))

print(digit_count(num))
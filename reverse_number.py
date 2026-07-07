def reverse_number(num):
    rev = 0
    digit = 0
    while(num>0):
        digit = num % 10
        rev = (rev*10) + digit
        num //= 10
    return rev

def reverse_string(str):
    rev = ""
    for i in range((len(str)-1),-1,-1):
        rev += str[i]
    return rev
num = int(input("Enter a number: "))
print(f"Original number: {num}")
print("Reversed number: ", reverse_number(num))

str = input("Enter a string: ")
print("Reverse by string method: ", reverse_string(str))
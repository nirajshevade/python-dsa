def palindrome_check(num):
    original_num = num
    rev = 0
    while(num > 0):
        digit = num % 10
        rev = (rev*10) + digit
        num //= 10
    if(rev == original_num):
        return "Yes, it is a Palindrome!"
    else:
        return "No, it is not a Palindrome!"

num = int(input("Enter a number: "))
print(palindrome_check(num))
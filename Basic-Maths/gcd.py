def gcd(num1, num2):
    gcd = 1
    for i in range(1, min(num1,num2)+1):
        if(num1 % i == 0 and num2 % i == 0):
            gcd = i
    return gcd 

# optimal
def find_gcd(num1, num2):
    while num1 > 0 and num2 > 0:
        if(num1 > num2):
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    if num1 == 0:
        return num2
    return num1

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("GCD: ", gcd(num1, num2))
print("GCD: ", find_gcd(num1, num2))
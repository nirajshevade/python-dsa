def armstrong_num(num):
    k = len(str(num))
    temp = num
    sum = 0
    while(num > 0):
        
        val = num % 10
        sum = sum + (val ** k)

        num //= 10
    if sum == temp:
        return True
    else:
        return False


num = int(input("Enter a number: "))
print(armstrong_num(num))

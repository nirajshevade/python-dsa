# def print_name(name, count):
#     while(count > 0):

#         print(name)
#         count -= 1

def printName(name, count, N):
    if count == N:
        return
    
    print(name)

    printName(name, count+1, N)



N = int(input("Enter number: "))
name = input("Enter Name: ")
printName(name, 0, N)
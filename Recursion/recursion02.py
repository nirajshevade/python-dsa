# def print_nums(count):
#     for i in range(1,count+1):
#         print(i)

def print_nums(current, N):
    
    if current > N:
        return
    
    print(current, end= ' ')

    print_nums(current+1, N)
N = int(input("Enter count: "))
print_nums(1, N)

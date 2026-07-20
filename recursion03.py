# def print_nums(count):
#     for i in range(count, 0, -1):
#         print(i)

def print_nums(current, N):
    
    if current < N:
        return
    
    print(current, end= ' ')

    print_nums(current-1, N)
current = int(input("Enter count: "))
print_nums(current, 1)

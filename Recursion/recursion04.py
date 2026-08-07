

def print_sum(current, N):
    if current > N:
        return 0

    return current + print_sum(current+1, N)
    
def print_sum_by_formula(N):
    sum = int((N * (N+1))/2)
    return sum

N = int(input("Enter count: "))
print("By recursion", print_sum(1, N))

print("By formula: ", print_sum_by_formula(N))
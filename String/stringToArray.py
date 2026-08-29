def stringToArray(str):
    char_array = list(str)
    return char_array

def reverseArray(arr):
    rev_arr = arr[::-1]
    return rev_arr
str = input("Enter String: ")
print(stringToArray(str))

arr = stringToArray(str)
print(reverseArray(arr))


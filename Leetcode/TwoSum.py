def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
    return [-1, -1]

nums = []
size = int(input("Enter size of number array:"))
for i in range(0, size):
    nums.append(int(input(f"Enter Element {i+1}: ")))
    
print(f"Array is: {nums}")
target = int(input("Enter target: "))

print(twoSum(nums, target))

    
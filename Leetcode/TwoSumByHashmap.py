def two_sum_by_hashmap(nums, target):
    
    seen = {}
    
    for i in range(len(nums)):
        comp = target - nums[i]
        
        if comp in seen:
            return [seen[comp],i]
        
        seen[nums[i]] = i
    return [-1,-1]
    


nums = []
size = int(input())
for i in range(0, size):
    nums.append(int(input()))
print(nums)
target = int(input())
print(two_sum_by_hashmap(nums, target))

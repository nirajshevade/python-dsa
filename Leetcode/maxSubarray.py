
def maxSubArray(nums):
    # BRUTE FORCE
    # max_sum = 0
    # for i in range(len(nums)):
    #     curr_sum = 0
    #     for j in range(i, len(nums)):
    #         curr_sum += nums[j]
    #         max_sum = max(max_sum, curr_sum)
    # return max_sum
    
    # OPTIMAL
    max_sum = nums[0]
    curr_sum = nums[0]
    
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], nums[i] + curr_sum)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum
    
    
nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))


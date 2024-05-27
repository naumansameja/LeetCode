def value(nums):
    nums.sort()
    smallest_difference = float('inf')
    for num in range(1, len(nums)):
        if abs(nums[num-1] - nums[num]) < smallest_difference:
            smallest_difference = abs(nums[num-1] - nums[num])
    return smallest_difference


print(value([100,1,10]))
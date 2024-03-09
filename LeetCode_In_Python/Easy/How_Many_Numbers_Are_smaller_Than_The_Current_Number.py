

def smaller_than_current(nums):
    n = len(nums)
    result = [0 for i in range(n)]
    new = sorted(nums)
    indices = {}
    for index in range(n):
        if new[index] not in indices:
            indices[new[index]] = index
    for index in range(n):
        result[index] = indices[nums[index]] 
    
    return result 

nums = nums = [8,1,2,2,3]
print(smaller_than_current(nums))
def repeating(nums):
    result = []
    for num in range(len(nums)):
        if nums[abs(nums[num])-1] < 0:
            result.append(abs(nums[num]))
        else:
            nums[abs(nums[num])-1] *= -1
    return result

nums = [4,3,2,7,8,2,3,1]
print(repeating(nums))
def remove_duplicates(nums):
    found = {}
    for num in nums:
        if num not in found:
            found[num] = None
    index = 0
    for key in found:
        nums[index] = key
        index += 1
    # for i in range(index, len(nums)):
    
    #     nums[i] = "_"
    
    return index

lst = [0,0,1,1,1,2,2,3,3,4]

print(remove_duplicates(lst))
print(lst)




class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        result = []
        start = nums[0]
        curr_string = str(nums[0])

        for num in range(1,len(nums)):
            if nums[num] != start+1:
                if nums[num-1] != int(curr_string):
                    result.append(curr_string + "->" + str(nums[num-1]))
                else:
                    result.append(curr_string)
                curr_string = str(nums[num])
            start = nums[num]

        if nums[num] != int(curr_string):
            result.append(curr_string + "->" + str(nums[num]))
        else:

            result.append(curr_string)
        return result
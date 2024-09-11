class Solution:
    def longestSubarray(self, nums) -> int:
        last_zero = None
        curr_length = 0
        max_length = 0
        left = right = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                last_zero = i
                zeros += 1
                # curr_length += 1
                break
            curr_length += 1
        if last_zero == None:
            return curr_length - 1


        right = last_zero+1
        while right < len(nums) and left < len(nums):
            if nums[right] == 0:
                max_length = max(curr_length, max_length)
                left = last_zero+1
                last_zero = right
                curr_length = right - left 
                right += 1
            else:
                curr_length += 1
                right += 1
        return max(max_length,curr_length)
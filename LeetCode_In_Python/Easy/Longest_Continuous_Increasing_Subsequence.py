class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        longest = 1
        current = 1
        for num in range(1,len(nums)):


            if nums[num-1] < nums[num]:
                current += 1

            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)
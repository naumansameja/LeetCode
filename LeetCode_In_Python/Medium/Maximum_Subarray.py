class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            cur_sum = max(nums[i]+cur_sum, 0)
            max_sum = max(max_sum, cur_sum)
        if max_sum == 0:
            return max(nums)
        return max_sum
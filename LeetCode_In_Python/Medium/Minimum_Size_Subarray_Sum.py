class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        curr_sum = 0
        left, right = 0,0
        curr_length = 0
        while right <= len(nums) and left < len(nums):
            if curr_sum >= target:
                curr_sum -= nums[left]
                left += 1
                min_length = min(min_length, curr_length)
                curr_length -= 1

            elif right < len(nums):
                curr_sum += nums[right]
                right += 1
                curr_length += 1
            else:
                right += 1
        
        if min_length == float('inf'):
            return 0
        return min_length
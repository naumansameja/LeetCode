class Solution:
    def longestOnes(self, nums, k: int) -> int:
        left = 0
        right = 0
        zeros = 0
        max_length = 0
        current_length = 0
        while right < len(nums) and left < len(nums):
            if nums[right] == 0:
                zeros += 1
                while zeros > k:
                    zeros -= nums[left] ^ 1
                    left += 1
                    max_length = max(current_length, max_length)
                    current_length -= 1
                
            current_length += 1
            right += 1
        
        return max(max_length, current_length)
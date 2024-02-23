class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0
        i = 0
        while i < len(nums):
            if nums[i] + i >= len(nums) - 1:
                return jumps + 1
            x = len(nums) - nums[i+1] - i+1
            k = i + 1
            for j in range(i+1, i+nums[i]+1):
                if j < len(nums):
                    if len(nums) - nums[j] - j <= x:
                        x = len(nums) - j -nums[j]
                        k = j
            i = k
            jumps += 1
            
        return jumps
        
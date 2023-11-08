class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        farthest = 0
        for i in range(len(nums)):
            farthest = max(farthest, i+nums[i])
            if farthest == i and nums[i] == 0:
                return False
            if farthest >= len(nums) - 1:
                return True
        return False
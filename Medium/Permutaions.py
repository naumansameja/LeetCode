class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
                return [nums]
        res = []
        for i in nums:
            number = i
            remaining = [j for j in nums if j != i]
            x = self.permute(remaining)
            for i in x:
                res.append([number] + i)
        return res
        
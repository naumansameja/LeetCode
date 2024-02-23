class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutations(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            res = []
            for i in range(len(nums)):
                letter = nums[i]
                remaining = [nums[j] for j in range(len(nums)) if j != i]
                lst = permutations(remaining)
                for j in lst:
                    x = [letter]+j
                    if x not in res:
                        res.append(x)
                    
                    
            return res
        return permutations(nums)
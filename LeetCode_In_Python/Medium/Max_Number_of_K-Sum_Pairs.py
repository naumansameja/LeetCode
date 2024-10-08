class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        ops = 0

        for num in nums:
            nums_dict[num] -= 1
            target = k - num
            if nums_dict[num] >= 0 and (target in nums_dict and nums_dict[target] > 0):
                nums_dict[target] -= 1
                ops += 1
            else:
                nums_dict[num] += 1

        return ops
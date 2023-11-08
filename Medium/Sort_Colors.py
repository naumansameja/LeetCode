class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        k = 0
        if 0 in d:
            for i in range(d[0]):
                nums[k] = 0
                k += 1
        if 1 in d:
            for i in range(d[1]):
                nums[k] = 1
                k += 1
        if 2 in d:
            for i in range(d[2]):
                nums[k] = 2
                k += 1
        return nums
        
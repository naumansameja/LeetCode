class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                if d[i] >= 2:
                    d.pop(i)
                else:
                    d[i] += 1
            else:
                d[i] = 1
        for i in d:
            return i
        
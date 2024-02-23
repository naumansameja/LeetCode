class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        result = []
        threshold = len(nums) // 3
        for num in counts:
            if counts[num] > threshold:
                result.append(num)
        return result
        
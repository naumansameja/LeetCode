class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Store all elements in a set
        found = set()
        for num in range(len(nums)):
            # If an element is zero, set it to infinity
            if nums[num] < 0:
                nums[num] = float('inf')
            found.add(nums[num])
        # Start from 1 and iterate until we find a missing element
        start = 1
        while True:
            if start not in found:
                return start
            start += 1
        
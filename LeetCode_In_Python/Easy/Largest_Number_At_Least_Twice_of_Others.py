class Solution:
    def dominantIndex(self, nums) -> int:
        maximum = 0
        second_max = 1

        for num in range(len(nums)):
            if nums[num] > nums[maximum]:
                second_max = maximum
                maximum = num
            elif nums[num] > nums[second_max] and num != maximum:
                second_max = num

        if nums[maximum] >= nums[second_max]*2:
            return maximum
        return -1
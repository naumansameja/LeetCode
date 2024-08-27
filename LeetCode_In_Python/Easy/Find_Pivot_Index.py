class Solution:
    def pivotIndex(self, nums) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for num in range(len(nums)):
            right_sum -= nums[num]
            if left_sum == right_sum:
                return num
            left_sum += nums[num]
        return -1
class Solution:
    def findErrorNums(self, nums):
        def get_duplicate(nums):
            for num in nums:
                if nums[abs(num)-1] < 0:
                    return abs(num)
                else:
                    nums[abs(num)-1] *= -1
        expected_sum = sum(range(len(nums)+1))
        actual_sum = sum(nums)
        dup = get_duplicate(nums)
        return [dup, expected_sum - actual_sum+dup]




        
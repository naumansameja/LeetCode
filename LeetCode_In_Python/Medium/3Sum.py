class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        for num in range(len(nums)):
            start = num+1
            end = len(nums) - 1
            while  start < end:
                if nums[start] + nums[end] + nums[num] > 0:
                    end -= 1
                    continue
                elif nums[start] + nums[end] + nums[num] < 0:
                    start += 1
                    continue
                else:
                    result.add((nums[start] , nums[end] , nums[num]))
                    start += 1
        # result = list(result)
        # for res in range(len(result)):
        #     result[res] = list(result[res])

        return result
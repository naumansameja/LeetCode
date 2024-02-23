class Solution:
    def topKFrequent(self, nums, k: int) :
        counts = {}
        distinct = 0
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                distinct += 1
        index = 0
        for key in counts:
            nums[index] = (key, counts[key])
            index += 1
        nums = nums[:distinct]
        nums.sort(key=self.sorting_criteria, reverse=True)
        nums = nums[:k]
        for index in range(len(nums)):
            nums[index] = nums[index][0]
        return nums

    def sorting_criteria(self,element):
        return element[1]
sol = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(sol.topKFrequent(nums, k))
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = dict()
        max_count = 0
        for num in range(len(nums)):
            if nums[num] in counts:
                counts[nums[num]][0] += 1
            else:
                counts[nums[num]] = [1,None,None]
            if counts[nums[num]][1] == None:
                    counts[nums[num]][1] = num
            counts[nums[num]][2] = num
            if counts[nums[num]][0] > max_count:
                max_count = counts[nums[num]][0]
        min_length = len(nums)
        for key, val in counts.items():
            if val[0] == max_count and val[2] - val[1] + 1 < min_length:
                min_length = val[2] - val[1] + 1

        return min_length
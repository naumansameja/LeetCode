class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        cur_sum = 0
        max_average = - float('inf')
        start = 0
        for num in range(k-1):
            cur_sum += nums[num]
        
        for num in range(k-1, len(nums)):
            cur_sum += nums[num]
            max_average = max(max_average, cur_sum/k)
            cur_sum -= nums[start]
            start += 1

            
        return max_average
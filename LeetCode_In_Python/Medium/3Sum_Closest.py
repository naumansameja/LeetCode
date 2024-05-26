class Solution:
    def threeSumClosest(self, nums, target: int):
        nums.sort()
        closest_difference = float('inf')
        closest_sum = None
        for num in range(len(nums)):
            start = num+1
            end = len(nums) - 1
            while  start < end:
                current_sum = nums[start] + nums[end] + nums[num]
                difference = self.calculate_difference(current_sum, target)
                if difference < closest_difference:
                    closest_difference = difference
                    closest_sum = current_sum
                
                if current_sum > target:
                    end -= 1
                    continue
                elif current_sum < target:
                    start += 1
                    continue
                else:
                    return current_sum

        return closest_sum

    def calculate_difference(self, current_sum, target):
        if (current_sum < 0 and target > 0) or (current_sum > 0 and target < 0):
            return abs(target-0) + abs(current_sum-0)
        return abs(target-current_sum)
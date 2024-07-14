class Solution:
    def nextPermutation(self, nums) -> None:
        if len(nums) == 1:
            return nums
        break_point = len(nums)-2
        while break_point >= 0:
            if nums[break_point] < nums[break_point+1]:
                break
            break_point -= 1
        if break_point == -1:
            nums.reverse()
            return

        curr = break_point + 1
        element = break_point + 1
        
        while curr < len(nums):
            if nums[curr] > nums[break_point] and nums[curr] <= nums[element]:
                element = curr
            curr += 1
        nums[break_point], nums[element] = nums[element], nums[break_point]
        last = len(nums)-1
        break_point += 1
        while last > break_point:
            nums[last], nums[break_point] = nums[break_point], nums[last]
            last -= 1
            break_point += 1
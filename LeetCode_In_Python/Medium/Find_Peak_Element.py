class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) ==1 :
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums)-1] > nums[len(nums)-2]:
            return len(nums) - 1
        def peak(nums):
            start = 1
            end = len(nums) - 1
            while start <= end:
                mid = (start+end)//2
                if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                    return mid
                elif nums[mid] < nums[mid+1]:
                    start = mid+1
                elif nums[mid] < nums[mid-1]:
                    end = mid-1
        return peak(nums)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(lst, target, left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                return binary_search(lst, target, mid+1, right)
            else:
                return binary_search(lst, target, left, mid-1)
        x = binary_search(nums, target, 0, len(nums)-1)
        if x == -1:
            return [-1,-1]

        l = x - 1
        r = x + 1
        while l >= 0:
            if nums[l] == target:
                l -= 1
            else:
                break
        while r <= len(nums)-1:
            if nums[r] == target:
                r += 1
            else:
                break
        return [l+1, r-1]

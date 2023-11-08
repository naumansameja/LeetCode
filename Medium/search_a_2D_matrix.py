class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(lst, target , left, right):
            if left > right:
                return False
            mid = (left + right) // 2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                return binarysearch(lst, target, mid+1, right)
            else:
                return binarysearch(lst, target, left, mid-1)
        mid = len(matrix) // 2
        upper = mid
        lower = mid
        while mid >= 0 and mid < len(matrix):
            if matrix[mid][len(matrix[mid])-1] == target or matrix[mid][0] == target:
                return True
            if matrix[mid][len(matrix[mid])-1] >= target and matrix[mid][0] <= target:
                break
            elif matrix[mid][0] > target:
                if mid-1 < lower:
                    lower = mid
                    mid = mid - 1
                else:
                    return False
                    
            elif matrix[mid][len(matrix[mid])-1] < target:
                if mid+1 > upper:
                    upper = mid
                    mid = mid+1
                else:
                    return False
                    
        if mid >= 0 and mid < len(matrix):
            return binarysearch(matrix[mid], target, 0, len(matrix[mid])-1)
        return False
        
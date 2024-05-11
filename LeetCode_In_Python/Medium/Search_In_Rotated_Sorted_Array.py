class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def modified_binary_search(array, elt, start, end):
            mid = (start+end)//2
            if array[mid] == elt:
                return mid
            if start >= end:
                return -1
            
            
            if array[mid+1] > array[end]:
                if array[start] <= elt and array[mid] >= elt:
                    return modified_binary_search(array, elt, start, mid-1)
                return modified_binary_search(array, elt, mid+1, end)
            
            if array[start] >= array[mid]:
                if array[mid+1] <= elt and array[end] >= elt:
                    return modified_binary_search(array, elt, mid+1, end)   
                return modified_binary_search(array, elt, start, mid-1)
            if array[mid+1] <= elt and array[end] >=  elt:
                return modified_binary_search(array, elt, mid+1, end)  
            return modified_binary_search(array, elt, start, mid-1)
        return modified_binary_search(nums, target, 0, len(nums)-1)
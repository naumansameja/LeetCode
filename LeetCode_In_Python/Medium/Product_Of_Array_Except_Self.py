# Approach
# If you find only one zero in the array, all elements other than that zero will have zero product.
# If you find two zeroes, all products will be zeroes because of multiplication with zero.
# If you find no zeroes, you can just use the product of entire array and the product at ith location will be the product_of_array/array[i].


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        first_zero_found = False
        
        for num in nums:
            
            if first_zero_found and num == 0:
                return [0] * len(nums)
                
            if num == 0:
                first_zero_found = True
                continue
            product *= num
        if first_zero_found:
            for num in nums:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
        else:
            for num in nums:
                res.append(int(product/num))
        return res
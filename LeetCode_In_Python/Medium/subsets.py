class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def make_permutations(nums, i=0):
            if i == len(nums)-1:
                return [[nums[i]]]
            lst = []
            lst.append([nums[i]])
            cur_list = make_permutations(nums, i+1)
            for element in cur_list:
                x = []
                x += element
                lst.append(x)
                element.append(nums[i])
                lst.append(element)
            return lst

        res = make_permutations(nums)
        res.append([])
        return res

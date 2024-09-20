# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root) -> int:
        def maximum_level_sum(root, level_sum, level=0):
            if root and level >= len(level_sum):
                level_sum.append(0)
            if root:
                level_sum[level] += root.val
                maximum_level_sum(root.left, level_sum,level+1)
                maximum_level_sum(root.right, level_sum, level+1)
            return level_sum
        max_level_val = -float('inf')
        max_level_index = 0
        for index, val in enumerate(maximum_level_sum(root,[])):
            if val > max_level_val:
                max_level_val = val
                max_level_index = index
        return max_level_index + 1


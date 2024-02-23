# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sum_root_to_leaf(root, sum=0):
            if root and not root.left and not root.right:
                return sum*10+root.val
            x = 0
            y = 0
            if root.left:
                x = sum_root_to_leaf(root.left, sum*10+root.val)
            if root.right:
                y = sum_root_to_leaf(root.right, sum*10+root.val)
            return x+y
        return sum_root_to_leaf(root)
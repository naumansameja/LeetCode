# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def left_most(root, val=0, val_level=0, level=1):
            if root:
                if level > val_level:
                    val = root.val
                    val_level = level
                val, val_level = left_most(root.left, val, val_level, level+1)
                val, val_level = left_most(root.right, val, val_level, level+1)
            return val, val_level
        return left_most(root)[0]
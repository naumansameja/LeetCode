# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root):
        def check_tree(root):
            if root:
                if root.val != self.val:
                    return False
                return check_tree(root.left) and check_tree(root.right)

            return True
        if root:
            self.val = root.val
            return check_tree(root)
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def flatten(root,lst):
            if root.left:
                flatten(root.left, lst)
            lst.append(root.val)
            if root.right:
                flatten(root.right, lst)

        def is_ascending(lst):
            i = 1
            while i < len(lst):
                if lst[i-1] >= lst[i]:
                    return False
                i += 1
            return True 
        lst = []
        flatten(root,lst)
        return is_ascending(lst)

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def right_view(root, l=0):
            if root:
                if len(lst) <= l:
                    lst.append(root.val)
                else:
                    lst[l] = root.val
                right_view(root.left, l+1)
                right_view(root.right, l+1)
        lst = []
        right_view(root)
        return lst
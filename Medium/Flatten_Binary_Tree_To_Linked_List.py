# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def convert(root):
            stack = [root]
            prev = None
            while stack:
                root = stack.pop()
                if root:

                    stack.append(root.right)
                    stack.append(root.left)
                    if prev:
                        prev.right = root
                        prev.left = None
                    prev = root
        convert(root)
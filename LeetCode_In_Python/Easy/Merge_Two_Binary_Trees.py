# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        def merge_two_trees(root,root1, root2):
            root = TreeNode()
            if root1 and root2:
                root.left = merge_two_trees(None, root1.left, root2.left)
                root.right = merge_two_trees(None, root1.right, root2.right)
                root.val = root1.val + root2.val
                return root

            elif root1:
                root.left = merge_two_trees(None, root1.left, None)
                root.right = merge_two_trees(None, root1.right, None)
                root.val = root1.val
                return root
            elif root2:
                root.left = merge_two_trees(None, None, root2.left)
                root.right = merge_two_trees(None, None, root2.right)
                root.val = root2.val
                return root
            return None
        return merge_two_trees(None, root1, root2)
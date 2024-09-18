# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        self.nodes = 0
        def good_nodes(root, max_encountered=-float('inf')):
            if root:
                if root.val >= max_encountered:
                    max_encountered = root.val
                    self.nodes += 1
                good_nodes(root.left, max_encountered)
                good_nodes(root.right, max_encountered)
        good_nodes(root)
        return self.nodes
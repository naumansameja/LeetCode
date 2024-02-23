# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowest_common_ancestor(root, p, q):
            if root:
                if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
                    return root
                elif p.val <= root.val and q.val <= root.val:
                    return lowest_common_ancestor(root.left, p, q)
                else:
                    return lowest_common_ancestor(root.right, p, q)
        return lowest_common_ancestor(root, p, q)
        

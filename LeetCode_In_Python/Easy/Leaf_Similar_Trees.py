# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        

        

        def get_leaves(root, leaves):
            if not root:
                return leaves
            if not root.left and not root.right:
                leaves.append(root.val)
                return leaves
            
            get_leaves(root.left, leaves)
            get_leaves(root.right, leaves)

            return leaves

        return get_leaves(root1,[]) == get_leaves(root2,[])
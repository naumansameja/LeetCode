# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kth_smallest(root, k, n=0):
            if root:
                n,found = kth_smallest(root.left, k, n)
                if found:
                    return n,True
                n += 1
                if n == k:
                    return root.val, True
                n,found = kth_smallest(root.right, k, n)
                if found:
                    return n,True
            return n,False
        return kth_smallest(root,k)[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root, k: int) -> bool:
        def two_sum_helper(root, current, k):
            if current:
                ans = search(root, current, k-current.val)
                left = two_sum_helper(root, current.left, k)
                right = two_sum_helper(root, current.right, k)
                return ans or left or right
            return False


        def search(root, current, k):
            if not root:
                return False
            if root.val == k and root != current:
                return True
            elif k > root.val:
                return search(root.right,current, k)
            elif k < root.val:
                return search(root.left,current, k)

        return two_sum_helper(root, root, k)
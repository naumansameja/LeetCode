# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root) -> int:
        self.tilt = 0
        def find_tilt(root, sum=0):
            if root:
                left_sum = find_tilt(root.left, sum)
                right_sum = find_tilt(root.right, sum)
                self.tilt += abs(left_sum-right_sum)
                return left_sum + right_sum + root.val



            return 0
        find_tilt(root)
        return self.tilt
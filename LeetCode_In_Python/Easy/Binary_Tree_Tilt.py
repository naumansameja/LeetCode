# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root):
        self.tilt = 0
        def find_tilt(root, sum=0):
            if root:
                val = root.val
                left_sum = find_tilt(root.left, sum)
                right_sum = find_tilt(root.right, sum)
                root.val = abs(left_sum-right_sum)
                self.tilt += root.val
                return left_sum + right_sum + val



            return 0
        find_tilt(root)
        return self.tilt

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right = TreeNode(9)
root.right.right = TreeNode(7)
s = Solution()
s.findTilt(root)
print(s.tilt)



class Solution:
    def diameterOfBinaryTree(self, root):
        self.max = 0
        def diameter(root):
            if root:
                left_height = diameter(root.left) +1
                right_height = diameter(root.right) + 1
                if left_height + right_height > self.max:
                    self.max = left_height + right_height 
                return max(left_height, right_height)
            return -1
        diameter(root)
        return self.max

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
s=Solution()
print(s.diameterOfBinaryTree(root))


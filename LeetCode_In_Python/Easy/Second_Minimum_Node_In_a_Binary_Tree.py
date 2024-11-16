# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root):
        self.second_mini = float('inf')
        self.minimum = float('inf')    
        self.second_minimun_helper(root)
        return self.second_min if self.second_min != float('inf') else -1
        
        

    def second_minimun_helper(self, root):
        if root:
            if root.val < self.minimum:
                self.second_min = self.minimum
                self.minimum = root.val

            elif root.val < self.second_min and root.val != self.minimum:
                self.second_min = root.val

            self.second_minimun_helper(root.left)
            self.second_minimun_helper(root.right)
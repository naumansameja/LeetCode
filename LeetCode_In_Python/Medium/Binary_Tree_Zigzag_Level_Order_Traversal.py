# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        def zigzag(root, level=0, lst=[]):
            if root:
                if level >= len(lst):
                    lst.append([])
                if level & 1:
                    lst[level].insert(0,root.val)
                else:   
                    lst[level].append(root.val)
                zigzag(root.left, level+1, lst)
                zigzag(root.right, level+1, lst)
            return lst
        return zigzag(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelordertraversal(root,l=0, lst=[]):
            if root == None:
                return []
            if l >= len(lst):
                lst.append([root.val])
            else:
                lst[l].append(root.val)
            if root != None:

                if root.left:
                    levelordertraversal(root.left,l+1, lst)
                if root.right:
                    levelordertraversal(root.right,l+1, lst)
            return lst
        return levelordertraversal(root)
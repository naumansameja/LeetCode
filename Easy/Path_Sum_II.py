# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def path_sum(root, sum,node_list, targetsum, res_lst=[]):
            if not root:
                return 
            if not (root.left or root.right):
                if root.val+sum == targetsum:
                    res_lst.append(node_list+[root.val])
                return res_lst
            path_sum(root.left, sum+root.val, node_list+[root.val], targetsum,res_lst)
            path_sum(root.right, sum+root.val, node_list+[root.val], targetsum,res_lst)

            return res_lst
        return path_sum(root, 0, [], targetSum)

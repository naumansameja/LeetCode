def path_sum(root, sum,node_list, targetsum, res_lst=[]):
    if not root:
        return res_lst
    if not (root.left or root.right):
        if root.val+sum == targetsum:
            res_lst.append(node_list+[root.val])
        return res_lst
    path_sum(root.left, sum+root.val, node_list+[root.val], targetsum,res_lst)
    path_sum(root.right, sum+root.val, node_list+[root.val], targetsum,res_lst)

    return res_lst




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = None
root = TreeNode(-2)
# root.left = TreeNode(2)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
root.right = TreeNode(-3)
# root.right.left= TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)
lst = path_sum(root, 0, [],-5)
print(lst)
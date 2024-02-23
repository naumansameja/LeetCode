# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete_Node(root, key):
            if root:
                if root.val == key:
                    if not root.right:
                        return root.left
                    if not root.left:
                        return root.right
                    else:
                        parent_node = root
                        node = root.right
                        while node.left:
                            parent_node = node
                            node = node.left
                        root.val = node.val
                        if parent_node == root:
                            root.right = node.right
                        else:
                            parent_node.left = node.right
                else:
                    if root.val > key:
                        root.left = delete_Node(root.left,key)
                    else:
                        root.right = delete_Node(root.right,key)
            return root
        return delete_Node(root,key)
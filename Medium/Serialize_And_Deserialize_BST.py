# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root) -> str:
        def serialize_tree(root, s=""):
            if root:
                s += str(root.val)+","
                s = serialize_tree(root.left,s)
                s = serialize_tree(root.right, s)
                return s
            s += "N,"
            return s
        return serialize_tree(root)
        

    def deserialize(self, data: str):
        def get_next(s, start, end):
            cur_s = ""
            while start < end:
                if s[start] == ",":
                    return cur_s,start+1
                cur_s += s[start]
                start += 1
        def deserialize_string(root, s, start, end):
            if start < end:
                cur_s,start = get_next(s,start,end)
                if cur_s == "N":
                    return None,start
                else:
                    root = TreeNode(int(cur_s))
                    root.left, start = deserialize_string(root, s,start,end) 
                    root.right, start = deserialize_string(root, s,start,end) 

            return root,start
        cur_s,start = get_next(data,0,len(data))
        if cur_s == "N":
            return None
        root = TreeNode(int(cur_s))
        return deserialize_string(root, data,0, len(data))[0]

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        def level_wise(node,d={}, l=0):
            if node:
                if l in d:
                    d[l].append(node)
                else:
                    d[l] = [node]
                d = level_wise(node.left, d, l+1)
                d = level_wise(node.right, d,l+1)
            return d
        def populate(d):
            for lst in d.values():
                for node in range(len(lst)-1):
                    lst[node].next = lst[node+1]
        d = level_wise(root)
        populate(d)
        return root
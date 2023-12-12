"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def height(root, depth=1):
            if not root:
                return 0
            max_depth = -float('inf')
            if depth > max_depth:
                max_depth = depth
            if root:
                for child in root.children:
                    h = height(child,depth+1)
                    if h > max_depth:
                        max_depth = h
                return max_depth
            return max_depth
        return height(root)
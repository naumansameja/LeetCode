"""
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone_graph(node, visited):
            if node:
                start = Node(node.val)
                visited[start.val] = start
                for neighbor in node.neighbors:
                    if neighbor.val not in visited:
                        visited[neighbor.val] = neighbor
                        new = clone_graph(neighbor, visited)
                    else:
                        new = visited[neighbor.val]
                    start.neighbors.append(new)
                return start
            return None


        return clone_graph(node, {})
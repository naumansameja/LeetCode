"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_map = {}
        itr = head
        while itr:
            node = Node(itr.val)
            nodes_map[itr] = node
            itr = itr.next
        itr = head
        while itr:
            nodes_map[itr].next = nodes_map.get(itr.next)
            nodes_map[itr].random = nodes_map.get(itr.random)
            itr = itr.next
        return nodes_map.get(head)

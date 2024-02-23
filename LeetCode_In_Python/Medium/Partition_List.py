# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        itr = head
        greater = ListNode(float("inf"))
        greater_head = greater
        smaller = ListNode(float('inf'))
        smaller_head = smaller
        while itr:
            next = itr.next
            itr.next = None
            if itr.val < x:
                smaller.next = itr
                smaller = smaller.next
            else:
                greater.next = itr
                greater = greater.next 
            itr = next
        smaller.next = greater_head.next
        return smaller_head.next
        
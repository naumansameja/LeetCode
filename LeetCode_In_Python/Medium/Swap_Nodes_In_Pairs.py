# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        itr = head
        while itr and itr.next:
            x = itr.val
            itr.val = itr.next.val
            itr.next.val = x

            itr = itr.next.next
        return head
        
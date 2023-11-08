# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        d = {}
        itr = head
        i = 1
        len = 1
        while itr:
            d[i] = itr
            itr = itr.next
            i += 1
            len += 1
        d[i] = itr
        n = len - n 
        if n-1 in d:
            d[n-1].next = d[n+1]
        else:
            head = d[n+1]
        return head
        
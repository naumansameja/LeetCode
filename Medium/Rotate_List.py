# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        l = 0
        itr = head
        while itr:
            if not itr.next:
                itr.next = head
                l += 1
                break
            l += 1
            itr = itr.next
        k = k % l
        k = l - k
        itr = head
        l = 0
        while True:
            if l == k-1:
                next = itr.next
                itr.next = None
                itr = next
                l += 1
                continue
            if l == k:
                return itr
            itr = itr.next
            l += 1
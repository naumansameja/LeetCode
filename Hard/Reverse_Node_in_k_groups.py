# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev = None
            cur = head
            i = 0
            while i < k :
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
                i += 1
            return prev, head
        if not head or not head.next:
            return head
        i = 1
        itr = head
        prev = None
        while itr:
            if i == k:
                if not prev:
                    cur = itr.next
                    first,last = reverse(head, k)
                    head = first
                    last.next = cur
                    prev = last
                    left = cur
                    itr = cur
                    i = 1
                    continue
                else:
                    cur = itr.next
                    first,last = reverse(left, k)
                    prev.next = first
                    last.next = cur
                    prev = last
                    left = cur
                    i = 1
                    itr = cur
                    continue
            i += 1
            itr = itr.next
        return head
        
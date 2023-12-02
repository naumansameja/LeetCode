# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def is_even(head, count):
            length = 0
            prev = None
            for i in range(count):
                if head:
                    prev = head
                    head = head.next
                else:
                    break
                length += 1
            return length & 1 != 1, prev
        def reverse_list(head, n):
            itr = head
            prev = None
            while n > 0 and itr:
                next = itr.next
                itr.next = prev
                prev = itr
                itr = next
                n -= 1 
            head.next = next
            return prev, head

        count = 1
        itr = head
        while itr:
            val, previous = is_even(itr, count)
            if val:
                prev.next, tail = reverse_list(itr, count)
                previous = tail
            count += 1
            prev = previous
            itr = prev.next
        return head
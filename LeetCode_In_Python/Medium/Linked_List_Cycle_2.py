# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d =set()
        itr = head
        while itr:
            if itr in d:
                return itr
            else:
                d.add(itr)
            itr = itr.next
        return None
        
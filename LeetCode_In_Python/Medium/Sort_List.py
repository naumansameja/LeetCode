# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        itr = head
        lst = []
        while itr:
            lst.append(itr.val)
            itr = itr.next
        lst.sort()
        head = ListNode(0)
        itr = head
        for i in lst:
            itr.next = ListNode(i)
            itr = itr.next
        return head.next
        
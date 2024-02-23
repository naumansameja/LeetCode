# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_list(head, left, right):
            prev = None
            itr = head
            for i in range(right-left+1):
                next_node = itr.next
                itr.next = prev
                prev = itr
                itr = next_node
            return prev,head
        itr = head
        prev = None
        for i in range(1,right+2):
            if i == left - 1:
                prev = itr
            elif i == left:
                left_node = itr
            elif i == right+1:
                right_node = itr
            if itr:
                itr = itr.next
        x = reverse_list(left_node, left, right)
        if not prev:
             head = x[0]
            
        else:
            prev.next = x[0]
        if right_node:
            x[1].next = right_node
        return head
        
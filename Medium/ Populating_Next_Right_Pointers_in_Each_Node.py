# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        end_list = ListNode(-1)
        end_head = end_list
        itr = head
        # current = 1
        while itr:
            # if current & 1: #if index is odd
            prev = itr
            if itr.next:

                end_head.next = itr.next
                itr.next = itr.next.next
                end_head = end_head.next
                end_head.next = None
                
            itr = itr.next
        prev.next = end_list.next
        return head
        
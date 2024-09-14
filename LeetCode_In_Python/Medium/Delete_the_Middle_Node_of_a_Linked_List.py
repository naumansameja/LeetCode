# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return head.next
        slow = head
        fast = head
        prev = slow

        while fast and fast.next:
            prev = slow
            slow = slow.next 
            fast = fast.next.next
        prev.next = slow.next
        return head
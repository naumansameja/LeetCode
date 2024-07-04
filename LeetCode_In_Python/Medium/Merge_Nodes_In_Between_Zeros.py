# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head):
        start = head
        result = start
        itr = head.next
        curr_sum = 0
        while itr:
            if itr.val == 0:
                start.next = ListNode(curr_sum)
                curr_sum = 0
                start = start.next

            else:
                curr_sum += itr.val
            itr = itr.next
        return result.next
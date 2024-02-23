# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        itr = list1
        n = 0
        while n <= b:
            if n == a - 1:
                start = itr
            if n == b:
                end = itr.next
            n += 1
            itr = itr.next
        start.next = list2
        itr = start 
        while itr:
            if itr.next == None:
                itr.next = end
                return list1
            itr = itr.next

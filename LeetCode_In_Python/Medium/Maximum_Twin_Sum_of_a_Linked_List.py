# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        stack = []
        itr = head
        while itr:
            stack.append(itr.val)
            itr = itr.next
        itr = head
        max_sum = 0
        n = len(stack)-1
        a = len(stack)//2
        for node in range(len(stack)-1,(len(stack)-1)//2,-1 ):
            max_sum = max((itr.val+stack[node]), max_sum)
            itr = itr.next
        return max_sum
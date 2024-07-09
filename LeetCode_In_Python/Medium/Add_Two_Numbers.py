# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode(None)
        res_itr = res
        carry = 0
        itr = l1
        itr2 = l2
        while itr or itr2 or carry:
            ans = 0
            if itr:
                ans += itr.val
                itr = itr.next 
            if itr2:
                ans += itr2.val
                itr2 = itr2.next
            ans += carry

            if ans >= 10:
                carry = 1
                ans = ans % 10
            else: 
                carry = 0
            res_itr.next = ListNode(ans)
            res_itr = res_itr.next

        return res.next
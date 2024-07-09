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
        while itr and itr2:
            ans = itr.val + itr2.val + carry
            if ans >= 10:
                carry = 1
                ans = ans % 10
            else: 
                carry = 0
            res_itr.next = ListNode(ans)
            res_itr = res_itr.next
            itr = itr.next 
            itr2 = itr2.next
        while itr:
            ans = itr.val + carry
            if ans >= 10:
                carry = 1
                ans = ans % 10
            else: 
                carry = 0
            res_itr.next = ListNode(ans)
            res_itr = res_itr.next
            itr = itr.next 
        while itr2:
            ans = itr2.val + carry
            if ans >= 10:
                carry = 1
                ans = ans % 10
            else: 
                carry = 0
            res_itr.next = ListNode(ans)
            res_itr = res_itr.next

            itr2 = itr2.next
        if carry:
            res_itr.next = ListNode(1)
        return res.next
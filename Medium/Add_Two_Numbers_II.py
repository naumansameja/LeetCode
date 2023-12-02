# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            previous = None
            itr = head
            while itr:
                next = itr.next
                itr.next = previous
                previous = itr
                itr = next
            return previous
        l1 = reverse(l1)
        l2 = reverse(l2)
        itr1 = l1
        itr2 = l2
        carry = 0
        prev = None
        while itr1 and itr2:
            num = itr1.val + itr2.val+carry
            itr1.val = (num)%10
            carry = num // 10
            prev = itr1
            itr1 = itr1.next
            itr2 = itr2.next
        # incase list1 ends first
        while itr2:
            num = itr2.val + carry
            if prev.next:
                prev.next.val = num % 10
            else:
                prev.next = ListNode(num%10)
            carry = num // 10
            prev = prev.next
            itr2 = itr2.next
        while itr1:
            num = itr1.val +carry
            itr1.val = (num)%10
            carry = num // 10
            prev = itr1
            itr1 = itr1.next
        if carry:
            prev.next = ListNode(carry)
        return reverse(l1)
        
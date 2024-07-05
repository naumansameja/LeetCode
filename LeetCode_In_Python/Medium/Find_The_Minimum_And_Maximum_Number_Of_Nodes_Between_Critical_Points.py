# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        itr = head.next
        prev = head
        current_index = 1
        first_minima = None
        minimum = float('inf')


        while itr.next:
            if (itr.val > itr.next.val and itr.val > prev.val) or (
                    itr.val < itr.next.val and itr.val < prev.val):

                prev = itr
                itr = itr.next
                first_minima = current_index
                prev_minima = first_minima
                current_index += 1
                break
            current_index += 1
            prev = itr
            itr = itr.next
        if first_minima == None:
            return [-1,-1]
        second_found = False
        while itr.next:
            if (itr.val > itr.next.val and itr.val > prev.val) or (
                    itr.val < itr.next.val and itr.val < prev.val):
                second_found = True
                if current_index - prev_minima< minimum:
                    minimum = current_index - prev_minima
                prev_minima = current_index
            prev = itr
            itr = itr.next
            current_index += 1
        if not second_found:
            return [-1,-1]
        maximum = prev_minima - first_minima
        return [minimum, maximum]
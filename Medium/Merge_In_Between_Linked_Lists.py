def merge(list1, list2, a, b):
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
     





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(0)
list1.next = ListNode(1)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(4)
list1.next.next.next.next.next = ListNode(5)
list1.next.next.next.next.next.next = ListNode(6)
list2 = ListNode(100000)
list2.next = ListNode(1000001)
list2.next.next = ListNode(1000002)
list2.next.next.next = ListNode(1000003)
list2.next.next.next.next = ListNode(1000004)
list1 = merge(list1, list2, 2,5)
print()
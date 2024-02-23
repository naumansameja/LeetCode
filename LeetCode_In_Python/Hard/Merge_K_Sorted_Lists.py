def merge(lists):
    new_list = []
    for node in lists:
        itr = node
        while itr:
            new_list.append(itr.val)
            itr = itr.next
    new_list.sort()
    head = ListNode(-1)
    itr = head
    for node in new_list:
        itr.next = ListNode(node)
        itr = itr.next
    return head.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
head3 = ListNode(2)
head2.next = ListNode(6)
lst = [head1, head2, head3]
head = merge(lst)
print()
def reorder(head):
    if not head or not head.next:
        return head
    
    # Storing the list in a stack and removing all links
    stack = []
    node =  head
    while node:
        next = node.next
        node.next = None
        stack.append(node)
        node = next

    # taking first element of stack as head of new linked list
    head = stack[0]
    # Making resultant list using two pointers
    end = len(stack)-1
    start = 1
    itr = head
    while start < end:
        itr.next = stack[end]
        itr.next.next = stack[start]
        itr = itr.next.next
        start += 1
        end -= 1
    if start == end:
        itr.next = stack[start]
    return head
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = reorder(head)
print()
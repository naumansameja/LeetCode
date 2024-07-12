class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        def middle_of_list(head):
            prev = None
            slow = head
            fast = head
            while fast and fast.next and fast.next.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return slow,prev
        def to_binary_tree(head):
            if not head:
                return head
            mid, prev = middle_of_list(head)
            root = TreeNode(mid.val)
            if prev:
                prev.next = None
                before = head
                root.left = to_binary_tree(before)
            else:
                root.left = None
            if mid.next:
                after = mid.next
                root.right = to_binary_tree(after)
            else:
                root.right = None
            
            
            
            
            return root
        return to_binary_tree(head)
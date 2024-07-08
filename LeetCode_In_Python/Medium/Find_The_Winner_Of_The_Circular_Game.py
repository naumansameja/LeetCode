class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        class Node:
            def __init__(self, data=None, next=None) -> None:
                self.data = data
                self.next = next
            

        def build_list(n):
            head = Node(1)
            itr = head
            for friend in range(2,n+1):
                itr.next = Node(friend)
                itr = itr.next
            itr.next = head
            return head,itr

        def winner(n, k):
            head,prev = build_list(n)
            out = 0
            start = 0
            itr = head
            while out < n-1:
                current = 1
                while current < k:
                    prev = itr
                    itr = itr.next
                    current += 1
                if itr == head:
                    head = itr.next
                    
                prev.next = itr.next
                out += 1
                itr = itr.next
            return head.data
        return winner(n,k)
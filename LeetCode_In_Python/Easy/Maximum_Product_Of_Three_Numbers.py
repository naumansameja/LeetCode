class Solution:
    def maximumProduct(self, nums) -> int:
        import heapq
        pos = heapq.nlargest(3,nums)
        neg = heapq.nsmallest(2,nums)
        print(pos,neg)

        return max(pos[0]* pos[1]* pos[2], pos[0]* neg[0]*neg[1])
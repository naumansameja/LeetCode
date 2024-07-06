class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current = time // (n-1)
        if current & 1:
            return n - (time % (n-1))
        return 1 + (time % (n-1))
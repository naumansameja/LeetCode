class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == time:
            return n - 1
        if n > time:
            return time + 1
        current = time // (n-1)
        if current & 1:
            return n - (time % (n-1))
        return 1 + (time % (n-1))
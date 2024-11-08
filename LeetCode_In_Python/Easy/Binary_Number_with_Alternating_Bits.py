class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        previous = n & 1
        n >>= 1
        while n:
            current = n & 1
            if not previous ^ current:
                return False
            previous = current
            n >>= 1
        return True
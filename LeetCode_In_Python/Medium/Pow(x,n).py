class Solution:
    def myPow(self, x: float, n: int) -> float:
        inc = x
        if n < 0:
            inc = 1/x
        for _ in range(abs(n-1)):
            x *= inc
        return x
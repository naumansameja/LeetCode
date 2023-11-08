class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            x = - (abs(dividend) // abs(divisor))
        else:
            x = dividend // divisor
        if x > 2**31 - 1:
            return 2**31 - 1
        elif x < - 2**31:
            return -2**31
        return x
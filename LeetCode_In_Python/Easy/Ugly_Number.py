class Solution:
    def isUgly(self, n: int) -> bool:
        def max_divide(n,d):
            if n < 1:
                return False
            while n % d == 0:
                n /= d


            return n

        n = max_divide(n,2)
        n = max_divide(n,3)
        n = max_divide(n,5)
        return n == 1
s = Solution()
print(s.isUgly(1))
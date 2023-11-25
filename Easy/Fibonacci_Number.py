class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fibonacci(n):
            if n == 0 or n == 1:
                return n
            num = 0
            if n-1 in d:
                num += d[n-1]
            else:
                d[n-1] = fibonacci(n-1)
                num += d[n - 1]
            
            if n-2 in d:
                num += d[n-2]
            else:
                d[n - 2] = fibonacci(n-2)
                num += d[n -2]
            return num
        d = {}
        return fibonacci(n)
        
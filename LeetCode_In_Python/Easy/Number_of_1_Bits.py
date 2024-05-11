class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        power = 0
        while (2 ** power) <= n:
            x  = (pow(2,power))
            if n & x != 0:
                counter += 1
            power += 1
        return counter
    


s = Solution()
print(s.hammingWeight(128))
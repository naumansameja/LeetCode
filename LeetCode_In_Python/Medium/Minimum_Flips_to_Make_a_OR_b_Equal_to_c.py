class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        d = {
            (0,0,0):0,
        (0,0,1):1,
          (0,1,0):1, 
          (0,1,1):0, 
          (1,0,0):1,
          (1,0,1):0,
          (1,1,0):2,
          (1,1,1):0

          }
        cost = 0
        while a or b or c:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1
            cost += d[(a_bit, b_bit, c_bit)]
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return cost
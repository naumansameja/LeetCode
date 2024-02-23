class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = ['' for i in range(numRows)]
        inc = True
        dec = False
        j = 0
        for i in s:
            lst[j] += i
            if j == numRows-1:
                dec = True
                inc = False
            elif j == 0:
                inc = True
                dec = False

            if inc:
                j += 1
            elif dec:
                if j > 0:
                    j -= 1
        s = ''
        for i in lst:
            s += i
        return s
        
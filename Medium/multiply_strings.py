class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i = 0
        num1_s = 0
        num2_s = 0
        l = max(len(num1), len(num2))
        while i < l:
            if i < len(num1):
                num1_s = 10 * num1_s + (ord(num1[i]) - 48)
            if i < len(num2):
                num2_s = 10 * num2_s + (ord(num2[i]) - 48)
            i += 1
        num1 = num1_s * num2_s
        if num1 == 0:
            return '0'
        s = ''
        while num1 > 0:
            s =  chr(48 + num1 % 10) + s
            num1 //= 10
        return s
        
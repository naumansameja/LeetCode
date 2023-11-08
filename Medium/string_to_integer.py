class Solution:
    def myAtoi(self, s: str) -> int:
        found = False
        res = '0'
        start = False
        for i in s:
            if i.isdigit():
                res += i
                found = True
            elif i.isalpha() or i == '.' or( found and (i in [' ', '+', '-', '.'])):
                break
            elif i in ['-','+']:
                res = i + res
                found = True
            elif i == ' ' :
                continue


        if int(res) <= -(2 **31):
            return -(2 **31 )
        elif int(res) >= (2 **31):
            return (2 **31 - 1)
        return int(res)
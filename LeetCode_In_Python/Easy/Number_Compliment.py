class Solution:
    def findComplement(self, num: int) -> int:
        binary = ''
        while num:
            if num & 1:
                binary = '0' + binary
            else:
                binary = '1' + binary

            num = num >> 1
        return int(binary, 2)
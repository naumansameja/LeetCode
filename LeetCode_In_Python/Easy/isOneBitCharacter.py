class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        curr_str = ''
        for bit in range(len(bits) - 1):
            if not curr_str and bits[bit] == 1:
                curr_str += str(bits[bit])

            elif curr_str:
                curr_str = ''
        return not curr_str

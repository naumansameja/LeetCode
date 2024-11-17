class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = ''
        for letter in s:
            if 64 < ord(letter) <= 90:
                new_s += chr(ord(letter)|32)
            else:
                new_s += letter

        return new_s
class Solution:
    def longestPalindrome(self, s: str) -> int:
        occurences = {}
        for character in s:
            if character in occurences:
                occurences[character] += 1
            else:
                occurences[character] = 1

        longest = 0
        is_odd = False
        for ocuurence in occurences:
            longest += ((occurences[ocuurence]//2)*2)
            if occurences[ocuurence] & 1 == 1:
                is_odd = True
        return longest + int(is_odd)
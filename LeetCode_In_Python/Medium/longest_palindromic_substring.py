class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        cur_s = ''
        for i in range(len(s)):
            for j in range(len(s), i-1, -1):
                cur_s = s[i:j] 
                if cur_s == cur_s[::-1] and len(cur_s) > len(longest):
                    longest = cur_s
        return longest
        
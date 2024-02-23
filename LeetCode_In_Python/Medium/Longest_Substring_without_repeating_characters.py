class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        longest_str = ''
        for i in range(len(s)):
            str = ''
            for j in range(i, len(s)):
                if s[j] not in str:
                    str += s[j]
                else:
                    break
            if len(str) > longest:
                longest = len(str)
                longest_str = str
        return longest
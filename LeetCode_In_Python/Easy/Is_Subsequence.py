class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        first = len(s)-1
        second = len(t)-1
        while first > -1 and second > -1:
            if t[second] == s[first]:
                first -= 1
            second -= 1
        return first == -1
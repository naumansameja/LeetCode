class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ''
        curr = ''
        for letter in str1:
            curr += letter
            if curr * int((len(str1)) / len(curr)) == str1 and curr * int(len(str2) / len(curr)) == str2:
                ans = curr
        return ans

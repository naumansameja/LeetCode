class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                b = s[left:right] == s[left:right][::-1]
                a = s[left + 1:right+1] == s[left + 1:right+1][::-1]
                return  a or b
            
            else:
                right -= 1
                left += 1


        return True

class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse_paranthesis(s,n, i=0):
            word = ''
            while True :
                if i == n or s[i] == ')':
                    return word,i
                elif s[i] == '(':
                    rev_word,i = reverse_paranthesis(s,n, i+1)
                    rev_word = rev_word[::-1]
                
                else:
                    rev_word = s[i]
                word = rev_word + word
                i += 1
        return reverse_paranthesis(s, len(s))[0][::-1]
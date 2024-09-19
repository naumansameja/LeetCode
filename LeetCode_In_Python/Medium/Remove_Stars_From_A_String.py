class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for character in s:
            if character == '*':
                stack.pop()
                continue
            stack.append(character)

        return ''.join(stack)
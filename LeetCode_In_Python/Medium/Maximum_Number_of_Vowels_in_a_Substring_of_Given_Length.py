class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        scores = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 0, 'h': 0, 'i': 1, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 1, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        left = 0
        right = 0
        curr_score = 0
        max_score = 0
        while left < len(s) and right < len(s):
            if right - left >= k:
                max_score = max(max_score, curr_score)
                curr_score -= scores[s[left]]
                left += 1
                
            else:
                curr_score += scores[s[right]]
                right += 1
        return max(max_score, curr_score)
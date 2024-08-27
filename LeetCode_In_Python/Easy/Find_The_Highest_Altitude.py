class Solution:
    def largestAltitude(self, gain) -> int:
        highest = current = 0
        for alt in gain:
            current += alt
            highest = max(highest, current)
        return highest
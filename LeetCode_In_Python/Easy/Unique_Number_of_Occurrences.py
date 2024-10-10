class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        from collections import Counter
        count = Counter(arr)
        return len(count.values()) == len(set(count.values()))
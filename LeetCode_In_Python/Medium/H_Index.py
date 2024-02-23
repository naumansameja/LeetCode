class Solution:
    def hIndex(self, citations: List[int]) -> int:
        d = {}
        for i in range(len(citations)+1):
            d[i] = 0
        for i in citations:
            for j in range(i+1):
                if j in d:
                    d[j] += 1

        max = 0
        for key in d:
            if key > max and d[key] >= key:
                max = key
        return max
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        possible_judges = {}
        no_possibility = set()
        for t in trust:
            no_possibility.add(t[0])
            if t[0] in possible_judges:
                possible_judges.pop(t[0])
            if t[1] not in no_possibility:
                if t[1] in possible_judges:
                    possible_judges[t[1]] += 1
                else:
                    possible_judges[t[1]] = 1
        for person in possible_judges:
            if possible_judges[person] == n-1:
                return person
        return -1
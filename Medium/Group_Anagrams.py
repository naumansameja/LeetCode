class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            x = ''.join(sorted(i))
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]


        res = []
        for i in d:
            res.append(d[i])
        return res
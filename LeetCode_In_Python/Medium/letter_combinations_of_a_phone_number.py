class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {'2':'abc','3':'def', '4':'ghi', '5':'jkl', '6':'mon', '7':'pqrs', '8':'tuv', '9':'wxyz' }

        lst = []
        for i in digits:
            lst.append(d[i])
        
        
        def all_combinations(lst, i):
            if len(lst) == i+1:
                return [j for j in lst[i]]
            
            res = []
            letters = lst[i]
            x = all_combinations(lst, i+1)
            for k in range(len(letters)):
                for l in range(len(x)):
                    res.append(letters[k] + x[l])
            return res
        res = all_combinations(lst, 0)
        return res
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        paths = [[0 for i in range(n)] for j in range(m)]
        paths[0][1] = 1
        paths[1][0] = 1

        
        for row in range(m):
            for col in range(n):
                curr_value = 0
                if row > 0:
                    curr_value = curr_value + paths[row-1][col]
                if col > 0:
                    curr_value = curr_value + paths[row][col-1]
                paths[row][col] = max(paths[row][col],curr_value)
        for row in paths:
            print(row)
        return paths[-1][-1]
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        if n == 1:
            sum_of_list = 0
            for row in range(n):
                for col in range(m):
                    sum_of_list += obstacleGrid[row][col]
            return 0 if sum_of_list > 0 else 1
        if m == 1:
            sum_of_list = 0
            for row in range(n):
                for col in range(m):
                    sum_of_list += obstacleGrid[row][col]
            return 0 if sum_of_list > 0 else 1

        
        for row in range(n):
            for col in range(m):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = -1
        if obstacleGrid[0][1] != -1:
            obstacleGrid[0][1] = 1
        if obstacleGrid[1][0] != -1:
            obstacleGrid[1][0] = 1

        
        for row in range(n):
            for col in range(m):
                if obstacleGrid[row][col] == -1:
                    continue
                curr_value = 0
                if row > 0 and obstacleGrid[row-1][col] != -1:
                    curr_value = curr_value + obstacleGrid[row-1][col]
                if col > 0 and obstacleGrid[row][col-1] != -1:
                    curr_value = curr_value + obstacleGrid[row][col-1]
                obstacleGrid[row][col] = max(obstacleGrid[row][col],curr_value)
        for row in obstacleGrid:
            print(row)
        return obstacleGrid[-1][-1]
class Solution:
    def minPathSum(self, grid) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                min = None
                if row > 0:
                    min = grid[row-1][col]
                if col > 0:
                    if not min or min > grid[row][col-1]:
                        min = grid[row][col-1]
                if min:
                    grid[row][col] += min
        return grid[-1][-1]
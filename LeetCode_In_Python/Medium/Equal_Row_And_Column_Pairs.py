class Solution:
    def equalPairs(self, grid) -> int:
        count = 0

        for outer_row in grid:
            for col in range(len(grid)):
                inner_col = []
                for row in range(len(grid)):
                    inner_col.append(grid[row][col])
                if inner_col == outer_row:
                    count += 1
        return count
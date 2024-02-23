class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indices = []
        def setzero(matrix, row, col):
            matrix[row] = [0 for i in matrix[row]]
            for i in range(len(matrix)):
                matrix[i][col] = 0
            return matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    indices.append((i,j))
        for index in indices:
            setzero(matrix, index[0], index[1])
        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            matrix[i], matrix[len(matrix)-i-1] = matrix[len(matrix)-i-1] , matrix[i]
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j],  matrix[j][i]= matrix[j][i], matrix[i][j]
        
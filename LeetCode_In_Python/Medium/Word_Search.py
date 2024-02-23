class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find(matrix, target):
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target[0]:
                        res = bfs(matrix, target, [(i,j,matrix[i][j],  ((i,j),))])
                        if res:
                            return res
            return False

        def bfs(matrix, target, q):
            while q:
                row, col, word, visited = q.pop()
                if word != target[:len(word)]:
                    continue
                if word == target:
                    return True
                if len(word) <  len(target):
                    if row + 1 < len(matrix):
                        if (row+1, col) not in visited:
                            q.append((row+1, col, word + matrix[row+1][col],visited +((row+1, col),)))
                    if row - 1 >= 0:
                        if (row-1, col) not in visited:
                            q.append((row-1, col, word + matrix[row-1][col], visited +((row-1, col),)))
                    if col+1 < len(matrix[row]):
                        if (row, col+1) not in visited:
                            q.append((row, col+1, word + matrix[row][col+1],visited +((row, col+1),)))
                    if col-1 >= 0:
                        if (row, col-1) not in visited:
                            q.append((row, col-1, word + matrix[row][col-1], visited +((row, col-1),)))

            return False
        return find(board, word)
        
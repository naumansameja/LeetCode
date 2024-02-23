def calculate_live_neighbors(matrix, row, col):
    moves = [(0,1),(0,-1), (1,-1),(1,0),(1,1),(-1,0),(-1,-1),(-1,1)]
    count = 0
    for new_row, new_col in moves:
        if (row+new_row < len(matrix) and row + new_row >= 0) and (col + new_col < len(matrix[0]) and col + new_col >= 0):
            count += matrix[row+new_row][col+new_col]

    return count
def game_of_life(board):
    convert_to_ones = []
    convert_to_zeroes = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            count = calculate_live_neighbors(board, row,col)
            if board[row][col] == 1 and count < 2 or count > 3:
                convert_to_zeroes.append((row,col))
            if board[row][col] == 0 and count == 3:
                convert_to_ones.append((row,col))
    for row,col in convert_to_ones:
        matrix[row][col] = 1
    for row,col in convert_to_zeroes:
        matrix[row][col] = 0
def print_matrix(matrix):
    for row in matrix:
        print(row)
            


matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
game_of_life(matrix)
print_matrix(matrix)
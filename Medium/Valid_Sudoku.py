class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        possible = {'1','2','3','4','5','6','7','8','9'}
    # validate all rows
    
        for row in range(9):
            existing = set()
            for column in range(9):
                element = board[row][column]
                if element == '.':
                    continue
                elif element in existing or element not in possible:
                    return False
                else:
                    existing.add(element)
        # validate all columns
        
        for row in range(9):
            existing = set()
            for column in range(9):
                element = board[column][row]
                if element == '.':
                    continue
                elif element in existing or element not in possible:
                    return False
                else:
                    existing.add(element)
        for outer_row in range(0,9,3):
            for outer_column in range(0,9,3):
                existing = set()
                for row in range(outer_row, outer_row+3):
                    for column in range(outer_column,outer_column+3):
                        element = board[column][row]
                        if element == '.':
                            continue
                        elif element in existing or element not in possible:
                            return False
                        else:
                            existing.add(element)
        return True
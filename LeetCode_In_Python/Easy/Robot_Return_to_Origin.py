class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves_sum = {}
        moves_sum['U'] = 0
        moves_sum['D'] = 0
        moves_sum['L'] = 0
        moves_sum['R'] = 0
        for move in moves:

            moves_sum[move] += 1

        return moves_sum['U'] == moves_sum['D'] and moves_sum['L'] == moves_sum['R']
class Solution:
    def candy(self, ratings: List[int]) -> int: 
            def left_shift(ratings,total):
                for i in range(1,len(ratings)):
                    if ratings[i] > ratings[i-1]:
                        total[i] = max(total[i-1]+1, total[i])
            def right_shift(ratings, total):
                for i in range(len(ratings)-2,-1,-1):
                    if ratings[i] > ratings[i+1]:
                        total[i] = max(total[i+1]+1, total[i])

            if len(ratings) == 1:
                return 1
            total = [1] * len(ratings)
            left_shift(ratings, total)
            right_shift(ratings, total)

            return sum(total)
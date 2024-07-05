class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return min(triangle[0])

        triangle[0] = [triangle[0]]
        for row in range(1,len(triangle)):
            for col in range(len(triangle[row])):
                lst = []
                if col != 0:
                    for element in triangle[row-1][col-1]:
                        lst.append(triangle[row][col] + element)
                if col != len(triangle[row]) - 1:
                    for element in triangle[row-1][col]:
                        lst.append(triangle[row][col] + element)

                triangle[row][col] = [min(lst)]

        
        return min(triangle[-1])[0]
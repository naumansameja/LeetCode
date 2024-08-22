class Solution:
    def sequentialDigits(self, low: int, high: int):
        def generate_number(start, n):
            num = ''
            for i in range(n):
                num += str(start)
                start += 1
            return int(num)





        def sequential_digits(low, high):
            import math
            num = int(round(math.log(low, 10),2)) + 1
            start = 1
            curr_num = 0
            ans = []
            while curr_num < high:
                if num == 9:
                    if low <= 123456789 <= high:
                        ans.append(123456789)
                    return ans
                if start > 10 - num:
                    num += 1
                    start = 1
                    continue

                curr_num = generate_number(start, num)
                start += 1
                if low <= curr_num <= high:
                    ans.append(curr_num)

            return ans

        return sequential_digits(low, high)
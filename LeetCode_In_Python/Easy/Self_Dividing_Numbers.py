class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        def is_self_dividing(n):
            new_n = n
            while new_n:
                if new_n % 10 == 0 or n % (new_n%10):
                    return False
                new_n //= 10

            return True

        numbers = []
        for num in range(max(1,left), right+1):
            if is_self_dividing(num):
                numbers.append(num)
        return numbers
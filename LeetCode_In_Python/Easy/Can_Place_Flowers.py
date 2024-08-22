class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        if len(flowerbed) == 1:
            return not flowerbed[0] == 1 or n == 0
        if not flowerbed[0] and not flowerbed[1]:
            n -= 1
            flowerbed[0] = 1
        x = flowerbed[0]
        for flower in range(1, len(flowerbed)-1):
            if not flowerbed[flower] and not x and not flowerbed[flower+1]:
                n -= 1
                flowerbed[flower] = 1
            x = flowerbed[flower]
        if not flowerbed[len(flowerbed) - 1] and not flowerbed[len(flowerbed) - 2]:
            n -= 1

        return n <= 0
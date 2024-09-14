class Solution:
    def successfulPairs(self, spells, potions, success: int):
        def search(potions, spell, success, left, right,min_found):
            if left > right:
                return min_found
            potion = (left + right) // 2
            if potions[potion] * spell >= success:
                min_found = potion
                return search(potions, spell, success, left, potion-1,min_found)
            else:
                return search(potions, spell, success, potion+1, right,min_found)

        success_counts = []
        potions.sort()
        for spell in spells:
            success_counts.append(len(potions)-search(potions, spell, success, 0, len(potions)-1, len(potions)))
        return success_counts
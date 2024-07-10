class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current_distance = 0
        for log in logs:
            if log == '../':
                current_distance -= 1
                current_distance = max(0,current_distance)
            elif log != './':
                current_distance += 1

        return current_distance
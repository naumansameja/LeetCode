class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0] * len(temperatures)
        for temperature in range(len(temperatures)):
            while stack and temperatures[temperature] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = temperature - index
            stack.append(temperature)
        return ans
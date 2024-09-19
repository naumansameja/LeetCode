class RecentCounter:

    def __init__(self):
        self.stack = []
        

    def ping(self, t: int) -> int:
        self.stack.append([t-3000, t])
        count = 0
        index = len(self.stack)-1
        while index >= 0 and (
            self.stack[index][1] >= t-3000 and self.stack[index][0] < t 
        ):
            count += 1
            index -= 1
        return count

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
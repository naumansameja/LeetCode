class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        if self.min > val:
            self.min = val
        self.stack.append(val)
        

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = float("inf")
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(a,b,operation):
            if operation == "+":
                return a + b
            if operation == '-':
                return b - a
            if operation == '*':
                return b * a
            
            return int(b / a)
        operations = {'+','-','/','*'}
        stack = []
        for token in tokens:
            if token in operations:
                stack.append(operate(stack.pop(),stack.pop(),token))
            else:
                stack.append(int(token))
        return stack.pop()





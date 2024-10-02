class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        index = 1
        curr_str = ''

        while index <= len(path):
            if index == len(path) or path[index] == '/':
                if curr_str == '..':
                    if stack:
                        stack.pop()
                elif curr_str == '.':
                    pass
                elif curr_str:
                    stack.append('/' + curr_str)
                curr_str = ''
                index += 1
                while index < len(path) and path[index] == '/':
                    index += 1

            else:
                curr_str += path[index]
                index += 1
        if not stack:
            return '/'
        path = ''
        for i in stack:
            path += i

        return path
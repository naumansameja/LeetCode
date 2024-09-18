class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numbers = set(['0','1','2','3','4','5','6','7', '8', '9'])
        paranthesis = set(['[',']'])
        curr_string = ''
        actual_string = ''
        index = 0
        while index < len(s):
            
            if s[index] == '[':
                if curr_string:
                    stack.append(curr_string)
                
                    curr_string = ''
                num_string = ''
                temp = index -1
                while temp >=0 and s[temp] in numbers:
                    num_string = s[temp] + num_string
                    temp -= 1
                if num_string:
                    stack.append(int(num_string))


                

            if s[index] not in paranthesis and s[index] not in numbers:

                curr_string +=  s[index]
            
            # if s[index] in numbers:
            #     if curr_string:
            #         stack.append(curr_string)
            #         curr_string = ''
            #     num_string = s[index]
            #     index += 1
            #     while s[index] in numbers:
            #         num_string += s[index]
            #         index += 1
            #     index -= 1
            #     stack.append(int(num_string))
            
            if s[index] == ']':
                if curr_string:
                    popped_str = curr_string
                    curr_string = ''
                else:
                    popped_str = ''
                while not isinstance(stack[-1],int):
                    popped_str = stack.pop() + popped_str
                stack.append(popped_str*stack.pop())


            index += 1
        temp = curr_string
        curr_string = ''
        while stack:
            if isinstance(stack[-1], int):
                curr_string *= stack.pop()
            else:
                curr_string = stack.pop() + curr_string


        return curr_string + temp
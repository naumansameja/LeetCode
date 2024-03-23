class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        cur_word = ''
        first_found = False
        find_res = False
        i = 0
        for letter in text:
            if find_res:
                if letter == ' ':
                    res.append(cur_word)
                    if cur_word == first and cur_word == second:
                        res.append(cur_word)
                    if cur_word == first:
                        first_found = True
                    cur_word = ""
                    find_res = False
                elif i == len(text)-1:
                    res.append(cur_word+letter)
                
                else:
                    cur_word += letter
            elif letter == ' ':
                if first_found and cur_word == second:
                    first_found = False
                    find_res = True
                    cur_word = ''
                else:
                    if cur_word == first:
                        first_found = True
                        cur_word = ''
                    else:
                        first_found = False
                        cur_word = ''
            else:
                cur_word += letter
            i += 1
        return res
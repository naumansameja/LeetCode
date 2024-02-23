def word_break(s, word, wordDict):
    
    
    if s == '':
        return True
    for i in s:
        if word in wordDict:
            x = word_break(s[len(word):], '',wordDict)
            if x:
                return True
        word += i
    return word in wordDict

    

def change(letter, d):
    if set(d[letter]) == set(d[letter][0]):
        d[letter] = d[letter][0]

s = "leetcode"
wordDict = ['leet', 'code']
can = False
for i in range(len(wordDict)):
    a = len(wordDict[i])
    b = len(s)
    if b % a == 0:
        can = True
        break 

if not can:
    print(False)
    exit()
for w in range(len(wordDict)):
    print(set(wordDict[0]))
    change(w, wordDict)
wordDict = set(wordDict)



print(word_break(s,'',wordDict))
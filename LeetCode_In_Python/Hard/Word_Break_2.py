class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.result = set()
        self.done = set()
        def wordbreak(s, wordDict,sentence="", word="", index=0):
            word = word+s[index]
            if index == len(s) -1:
                if word in wordDict:
                    self.result.add(sentence+word)
                return
            if word in wordDict:
                if sentence+word not in self.done:
                    self.done.add(sentence+word)
                    wordbreak(s,wordDict, sentence+word+" ", '', index+1)
                    wordbreak(s,wordDict, sentence, word, index+1)
            wordbreak(s, wordDict, sentence, word, index+1)
        wordbreak(s, set(wordDict))
        return list(self.result)

        
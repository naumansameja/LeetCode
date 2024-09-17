class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        words = {}
        curr = ''
        for word in searchWord:
            curr += word
            words[curr] = []

        possibles = products
        ans = []
        word = ''
        for index in range(len(searchWord)):
            
            word += searchWord[index]
            for product in possibles:
                if index >= len(product):
                    continue
                if product[index] == word[index]:
                    words[word].append(product)
            possibles = words[word]
        for word in words:
            x = words[word]
            ans.append(words[word][:3])
        return ans
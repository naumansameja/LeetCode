class RandomizedSet:

    def __init__(self):
        self.current_index = 0
        self.data = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        if self.current_index < len(self.data):
            self.data[self.current_index] = val
            self.hash[val] = self.current_index
        else:
            self.hash[val] = len(self.data)
            self.data.append(val)
        self.current_index += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        last_elem = self.data[self.current_index-1]
        remove_index = self.hash[val]
        self.data[remove_index], self.data[self.current_index-1] = self.data[self.current_index-1],self.data[remove_index] 
        self.hash[last_elem] = remove_index
        self.current_index -= 1
        self.hash.pop(val)
        return True
        

    def getRandom(self) -> int:
        import random
        return self.data[random.randint(0,self.current_index-1)]
    

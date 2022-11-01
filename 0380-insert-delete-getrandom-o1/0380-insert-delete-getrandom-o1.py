
class RandomizedSet:
    
    def __init__(self) -> object:
        self.randomSet = {} #val:insertionOrder
        self.vals = []
    
    def insert(self, val:int) -> bool:
        
        if val not in self.randomSet:
            self.randomSet[val] = len(self.randomSet)
            self.vals.append(val)
            return True
        else:
            return False
        
    def remove(self, val:int) -> bool:
        
        if val in self.randomSet:
            
            idx = self.randomSet[val]
            
            last_val = self.vals[-1]
            self.vals[idx] = last_val
            self.vals.pop()
            self.randomSet[last_val] = idx
            
            del self.randomSet[val]
            return True
        
        else:
            return False
    
    def getRandom(self) -> int:

        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
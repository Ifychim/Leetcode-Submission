import random
class RandomizedSet:

    def __init__(self):
        self.rand_set = set()

    def insert(self, val: int) -> bool:
        
        if val not in self.rand_set:
            self.rand_set.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        
        if val in self.rand_set:
            self.rand_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        
        list_set = list(self.rand_set)
        
        rand_idx = random.randint(0,len(list_set)-1)
        
        return list_set[rand_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
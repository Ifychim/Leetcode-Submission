import random
class RandomizedSet:

    def __init__(self):
        self.val_map = {} #key = insertion value, val = insertion order
        self.val_list = [] #keeps track of inserted/removed values
        
        

    def insert(self, val: int) -> bool:
        
        if val not in self.val_map:
            self.val_map[val] = len(self.val_list)
            self.val_list.append(val)
           
            return True
        
        else:
            return False

    def remove(self, val: int) -> bool:
        
        #we need to store the idx we want to remove from the array
        if val in self.val_map:
            
            removal_idx = self.val_map[val]
           
            #swapping elements in list and poppint
            last_val = self.val_list[-1]
            self.val_list[removal_idx] = last_val
            self.val_list.pop()
            
            #[1, 4, 3] [1,2,3,4]
            #{1:0, 3:2, 4:1} {1:0, 2:1, 3:2, 4:3}
            
            #updating dict key/vals and deleting element to be removed from map 
            self.val_map[last_val] = removal_idx
            del self.val_map[val]
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        
        rand_idx = random.randint(0,len(self.val_list)-1)
        
        return self.val_list[rand_idx]

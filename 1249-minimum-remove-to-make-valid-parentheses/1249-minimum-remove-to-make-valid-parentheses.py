class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        new_str = list(s) #convert string to list for processing
        counter = 0 #to keep track of parenthesis balancing
        result = ""
        
        #scan to balance open parenthesis
        for i in range(0,len(new_str)):
            
            if new_str[i] == "(":
                counter += 1
            
            elif new_str[i] == ")":
                #decrement counter to ensure that the parenthesis is balanced
                if counter > 0:
                    counter -=1
                else:
                    #mark element for deletion
                    new_str[i] = 0
                    
        counter = 0
        #scan to balance closed parenthesis
        for i in range(len(new_str)-1,-1,-1):
            
            if new_str[i] == ")":
                counter += 1
            
            elif new_str[i] == "(":
                #decrement counter to ensure that the parenthesis is balanced
                if counter > 0:
                    counter -=1
                else:
                    #mark element for deletion
                    new_str[i] = 0        
            
        
        for char in new_str:
            if char != 0:
                result += char
                
        return result
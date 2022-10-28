class Solution:
    def isValid(self, s: str) -> bool:
        
        #closed brackets encountered must match *dictionary* 
        #last open bracket encountered *stack*

        open_stack = []
        
        closed_matches = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            
            if char not in closed_matches:
                open_stack.append(char)
            else:
                
                if len(open_stack) > 0 and closed_matches[char] == open_stack[-1]:
                    open_stack.pop()
                else:
                    return False

        #every open bracket must have a corresponding closed bracket.

        if len(open_stack) == 0:
            return True
        else:
            return False
class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {')':'(', '}':'{', ']':'[' }
        
        open_brackets = []
        
        
        for bracket in s:
            
            if bracket not in brackets:
                
                open_brackets.append(bracket)
                
            else:
                
                if len(open_brackets) > 0 and open_brackets[-1] == brackets[bracket]:
                    open_brackets.pop()
                else:
                    return False
                
                
        if len(open_brackets) == 0:
            return True
        else:
            return False
                
            
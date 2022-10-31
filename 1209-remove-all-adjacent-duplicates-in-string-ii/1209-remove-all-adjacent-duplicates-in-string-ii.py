class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #stack solution

        stack = [] #[char, count]
        
        #Add characters in stack sequentially. 
        #Set char count to 1 if char not in stack
        #Increment char count if stack is not empty and current char is in stack
        
        for char in s:

            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
                
        #If the character at the top of our stack has a count of k, pop pair from stack.
            if stack[-1][1] == k:
                stack.pop()
        
        res = ""   
        
        for chars in stack:
            
            char,val = chars
            
            res += char*val
            
        return res
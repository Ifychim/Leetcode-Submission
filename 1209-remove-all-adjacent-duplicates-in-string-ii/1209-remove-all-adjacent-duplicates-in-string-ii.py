class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        res = ""
        for char in s:
            
            #check to see if top of our stack contains k chars
            if stack and stack[-1][1] == k:
                stack.pop()
                
            #if the character at the top of our stack is equivalent to current, update count
            #else, add character to stack and initialize count to one
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char,1])
                
        if stack and stack[-1][1] == k:
            stack.pop()
                                
        print(stack)
        
        for char,freq in stack:
            res += char * freq
            
        return res
                
            
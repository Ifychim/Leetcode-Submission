class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #stack and a hashmap solution
        
        #char_count = {}
        
        stack = [] #[char, count]
        
        #add characters in stack sequentially.
        #if the character we are adding in our stack has a count of k,
        #we pop k characters and decerement count in dict.
        
        for char in s:
            
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        res = ""   
        
        for chars in stack:
            
            char,val = chars
            res += char*val
            
        return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = [] #[temp,idx]
        
        for i,t in enumerate(temperatures):
            
            #if incoming value is greater than top of stack keep popping from top
            while stack and t > stack[-1][0]:
                temp,idx = stack.pop()
                diff = i - idx
                result[idx] = diff
                
                
            stack.append([t,i])
            
        return result
        
        
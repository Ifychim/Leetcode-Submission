class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) <= 1: return intervals
        
        sorted_intervals = sorted(intervals, key = lambda x: x[0]) #sort input by starting times
        
        stack = []
        stack.append(sorted_intervals[0]) #holds most recently added interval
        

        #go through the remaining intervals to check if overlap occurs.
        #overlap occurs when top of stack end time >= curr intervals start time
        for i in range(1,len(sorted_intervals)):
            
            stack_top = stack[-1]
            stack_start, stack_end = stack_top
            
            curr_interval = sorted_intervals[i]
            curr_start, curr_end = curr_interval
            
            #if an overlap occurs, create new interval, pop from stack and append new interval
            if stack_end >= curr_start:
                new_interval = [min(curr_start,stack_start), max(stack_end, curr_end)]
                stack.pop()
                stack.append(new_interval)
            else:
                stack.append(curr_interval)
                
                
        return stack
            
            
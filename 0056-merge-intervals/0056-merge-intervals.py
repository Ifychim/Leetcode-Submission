class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1: return intervals
       
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        
        #result contaning merged intervals in sorted order. 
        #We will need to reference the top of stack to see if a merge is required
        result = []
        result.append(sorted_intervals[0])
        
        
        for i in range(1,len(sorted_intervals)):
            
            #if merge is needed, pop from top of stack, append new interval
            #if merge not needed, append current interval to the stack
            
            top = result[-1]
            top_start, top_end = top
            curr_start, curr_end = sorted_intervals[i]
            
            if top_start == curr_start or top_end == curr_end or top_end == curr_start:
                merged = [min(top_start,curr_start), max(top_end,curr_end)]
                result.pop()
                result.append(merged)
            elif top_start < curr_start and top_end > curr_start:
                merged = [min(top_start,curr_start), max(top_end,curr_end)]
                result.pop()
                result.append(merged)
            elif top_start < curr_start and top_end > curr_end:
                merged = [min(top_start,curr_start), max(top_end,curr_end)]
                result.pop()
                result.append(merged)
            else:
                result.append(sorted_intervals[i])
                
        return result
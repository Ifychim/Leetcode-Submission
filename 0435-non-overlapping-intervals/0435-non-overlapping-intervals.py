class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #[[1,2],[1,3],[2,3],[3,4]] #if there is not an overlap with top of stack, append to stack
        
        if len(intervals) == 1: return 0
        
        res = []
        overlaps = 0
        
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        
        res.append(sorted_intervals[0])
        
        for i in range(1,len(sorted_intervals)):
            
            top, curr = res[-1], sorted_intervals[i]
            first_start, first_end = top
            curr_start, curr_end = curr
            
            if first_end > curr_start:
                #remove the interval with larger end value
                if first_end > curr_end:
                    res.pop()
                    res.append(curr)
                else:
                    continue
            else:
                res.append(curr)
        
    
        return len(intervals) - len(res)
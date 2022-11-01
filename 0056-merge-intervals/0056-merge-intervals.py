class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #sort interval in ascending order by start times
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        
        result = [sorted_intervals[0]]
        
        #starting from second interval, iterate through sorted intervals and check for overlap
        
        for i in range(1,len(sorted_intervals)):
            
            curr = sorted_intervals[i]
            curr_start, curr_end = curr[0], curr[1]
            
            #end value of most recently added interval depicts overlap.
            prev_end = result[-1][1]
            
            if prev_end >= curr_start:
                result[-1][1] = max(curr_end, prev_end)
            else:
                result.append(curr)
        
        
        return result
        
        
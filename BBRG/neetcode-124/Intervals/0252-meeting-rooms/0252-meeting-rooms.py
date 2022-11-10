class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
       
        if len(intervals) <= 1:
            return True
        
        sorted_intervals = sorted(intervals, key = lambda x: x[0]) #sort intervals by their start times
        
        a = 0
        b = 1
        
        
        while b < len(sorted_intervals):
            
            first = sorted_intervals[a]
            second = sorted_intervals[b]
            
            first_start, first_end = first
            second_start, second_end = second
            
            #three types of overlaps but, can be simplified by just looking at end values
            if first_end > second_start: return False
            #if first_start == second_start or first_end == second_end: return False
            #elif first_start < second_start and first_end > second_start: return False
            #elif first_start < second_start and first_end > second_end: return False
        
            
            a += 1
            b += 1
            
        return True
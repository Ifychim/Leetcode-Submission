class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) == 1: return True
        
        
        #we need to check if there are any overlaps between the time intervals
        #sorting the input in an ascending order by start time is the crucial first step
        
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        '''
        4 cases of overlaps: draw time diagram
        '''
        fast = 1
        slow = 0
        print(sorted_intervals)
        while fast < len(sorted_intervals):
            
            first_interval = sorted_intervals[slow]
            first_start, first_end = first_interval
            
            second_interval = sorted_intervals[fast]
            second_start, second_end = second_interval
            
            if first_start < second_start and first_end > second_end: return False
            elif first_start < second_start and first_end > second_start: return False
            #elif first_start >= second_start and first_end > second_end: return False
            elif first_start == second_start and first_end == second_end: return False
            else:
                fast += 1
                slow += 1
        
        return True
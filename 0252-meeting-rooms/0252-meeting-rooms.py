class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals) == 1:
            return True
        
        #sort intervals by starting time,
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        
        #two pointer technique to check for interval over laps
        
        first = 0
        second = 1
        
        while second < len(sorted_intervals):
            
            int1_start, int1_end = sorted_intervals[first]
            int2_start, int2_end = sorted_intervals[second]
            
            #if there is overlap return false
            if int2_end - int1_end <= 0 or int2_start < int1_end:
                return False
            
            first += 1
            second += 1
            
        print(sorted_intervals)
        return True
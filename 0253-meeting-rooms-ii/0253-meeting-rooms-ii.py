class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #idea is to find out how many rooms we will need at any given point in time.
        
        #by keeping track of start and end times, we can do the aforementioned
        
        start_times = []
        end_times = []
        
        for times in intervals:
            s,e = times
            
            start_times.append(s)
            end_times.append(e)
            
        start_times.sort()
        end_times.sort()
        #0,5,15
        #10,20,30
        result, num_meetings = 0, 0
        start, end = 0, 0 #two pointers to keep track of start and end times.
        #idea is if start time is smaller, than end time, we need another room so increment meetings 
        #if end time is larger, we finished with a meeting so decrement meetings.
        
        while start < len(start_times):
            
            if start_times[start] < end_times[end]:
                num_meetings += 1
                start += 1
            else:
                num_meetings -= 1
                end += 1
            #compute the maximum amount of meeting rooms we need
            result = max(result,num_meetings)
            
        return result
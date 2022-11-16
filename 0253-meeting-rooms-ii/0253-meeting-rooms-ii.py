import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) <= 1: return 1
        
        min_times = [] #heap to store min-end-times
        heapq.heapify(min_times)
        
        sorted_intervals = sorted(intervals, key = lambda x : x[0])
        
        heapq.heappush(min_times, sorted_intervals[0][1])
        
        
        #iterate through the remaining intervals, and check if we will need extra rooms or not
        
        for i in range(1, len(sorted_intervals)):
            
            curr_interval = sorted_intervals[i]
            curr_start, curr_end = curr_interval
            
            min_end = min_times[0] #current minimum end-time will always be root of the min-heap
            
            #if incoming start time is greater than minimum end time we need to pop the min end and add new                 min-end
            if curr_start >= min_end:
                heapq.heappop(min_times)
                heapq.heappush(min_times, curr_end)
            elif curr_start < min_end:
                #here is where an overlap occurs so we just need to append a new time slot to our heap
                heapq.heappush(min_times, curr_end)
                
        #after all is said and done, the length of our heap represents the max # of rooms needed at any point
        return len(min_times)
            
            
        
        
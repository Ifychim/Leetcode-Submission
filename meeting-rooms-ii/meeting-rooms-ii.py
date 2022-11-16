import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #we want to consistently know the earliest time when meetings will end
        #if an incoming meetings' start time is less than the minimum end time, then we know that we need another room
        #if the incoming meetings start time is greater than the min end time, we can re-use the room
        #to keep track of minimum ending times, we use a min-heap
        min_times = []
        heapq.heapify(min_times) #O(n)
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0]) #sorted by start times
        
        heapq.heappush(min_times,sorted_intervals[0][1])
    
        for i in range(1,len(sorted_intervals)):
            
            curr = sorted_intervals[i]
            curr_start,curr_end = curr
            
            #overlap occurs when incoming start time is less than min end time. append to heap
            if curr_start < min_times[0]:
                heapq.heappush(min_times,curr_end)
            elif curr_start >= min_times[0]:
                #we can re-use room if incoming start is >= min-end
                heapq.heappop(min_times)
                heapq.heappush(min_times, curr_end)
                
        return len(min_times)
            
        
        
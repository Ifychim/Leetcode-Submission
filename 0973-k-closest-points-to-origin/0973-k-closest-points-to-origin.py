import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #intuition is to find the distance between the given points and the origin
        #we can then store these these distances in a max heap. 
        #we can then return the first k points
        
        closest_points = []
        result = []
        heapq.heapify(points)
        
        for point in points:
            
            x, y = point
            
            origin_distance = math.sqrt((math.pow(x,2) + math.pow(y,2)))
            print(origin_distance)
            heapq.heappush(closest_points, (origin_distance * -1, point))
            
        while len(closest_points) > k:
            heapq.heappop(closest_points)
            
        for i in range(len(closest_points)):
            result.append(closest_points[i][1])
            
        return result
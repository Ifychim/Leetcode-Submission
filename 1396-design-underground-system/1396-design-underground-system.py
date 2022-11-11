class UndergroundSystem:
    
    def __init__(self):
        self.database = {}#hashmap to handle customer data and checking-in/out
        self.travel_times = []
        pass
    
    def checkIn(self, id: int, stationName: str, t:int) -> int:
        #only check in customers who are not already in the database (by id) 
        
        if id not in self.database:
            self.database[id] = [id, stationName, t]
        else:
            return
    
    def checkOut(self, id: int, stationName: str, t:int) -> int:
        #only check out customers who are already in the database (by id)
        #at check out we can computer the time it took to go from station A to station B
        
        if id in self.database:
            time_elapsed = t - self.database[id][2]
            
            #check-in station ,check-out station, time_elapsed
            self.travel_times.append([self.database[id][1],stationName, time_elapsed])
            del self.database[id]

        else:
            return
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        # sum of times / number of times specified path was traveled
        
        sum_of_times = 0
        path_frequency = 0
        
        for times in self.travel_times:
            
            start, end, time_elapsed = times
            
            if start == startStation and end == endStation:
                path_frequency += 1
                sum_of_times += time_elapsed
        
        return sum_of_times / path_frequency
                
        
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
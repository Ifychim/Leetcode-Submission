from collections import defaultdict
class UndergroundSystem:
    
    def __init__(self):
        self.user_data = defaultdict(list) #cust_id:[id,station,time]
        #self.station_data = defaultdict(list)#cust_id:[startStation,endStation, time_difference]
        self.station_data = [] #[startStation,endStation, time_difference]
    def checkIn(self, id: int, stationName: str, time: int) -> None:
        
        #if customer is already in system return, else we add them to the system
        if id in self.user_data:
            return
        else:
            self.user_data[id].append(id)
            self.user_data[id].append(stationName)
            self.user_data[id].append(time)
    
    def checkOut(self, id: int, stationName: str, time: int) -> None:
        
    #if customer is in the system and station name is different then check them out, else do nothing
        if id in self.user_data and self.user_data[id][1] != stationName:
        
            #self.station_data[id].append(self.user_data[id][1])
            #self.station_data[id].append(stationName)
            #self.station_data[id].append(time - self.user_data[id][2])
            self.station_data.append([self.user_data[id][1], stationName, time - self.user_data[id][2]])
            del self.user_data[id]
        else:
            return
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        #sum of all time differences / #times
        times = []
    
        #for station_data in self.station_data.values():
        for station_data in self.station_data:
            start, end, time_diff = station_data
            
            if startStation == start and endStation == end:
                times.append(time_diff)
                
        return sum(times) / len(times)
    
    


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
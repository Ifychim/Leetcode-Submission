from collections import defaultdict
class UndergroundSystem:
    
    def __init__(self):
        self.user_data = defaultdict(list) #cust_id:[id,station,time] -> Handles users in system
        self.station_data = [] #[startStation,endStation, time_difference] -> Holds checkout data
        
    def checkIn(self, id: int, stationName: str, time: int) -> None:
        
        #if customer not in system check them in, else do nothing
        if id not in self.user_data:
            self.user_data[id].append(id)
            self.user_data[id].append(stationName)
            self.user_data[id].append(time)
        else:
            return
    
    def checkOut(self, id: int, stationName: str, time: int) -> None:
        
    #if customer is in the system and then check them out & collect data(start,end,time_diff), else do nothing
        if id in self.user_data:
            self.station_data.append([self.user_data[id][1], stationName, time - self.user_data[id][2]])
            del self.user_data[id]
        else:
            return
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #sum of all time differences / #times
        times = []
    
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
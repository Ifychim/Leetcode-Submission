class UndergroundSystem:
    
    def __init__(self,) -> object:
        self.cust_data = {} #id:[id,stationName, time]
        self.checkout_data = [] #[startStation, endStation, TimeDiff]
    def checkIn(self, id: int, stationName: str, t: int) -> None:
    
        if id not in self.cust_data:
            self.cust_data[id] = [id,stationName,t]
           
            return
        else:
            return
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        #if customer is checked in, check them out
        if id in self.cust_data:
            time_diff = t - self.cust_data[id][2]
            start_station, end_station = self.cust_data[id][1], stationName 
            
            self.checkout_data.append([start_station, end_station, time_diff])
            del self.cust_data[id]
            return
        else:
            return
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #iterate through out checkout data, sum up all time differences then divide by #events.
        avg = 0
        num_events = 0
        
        for event in self.checkout_data:
            start_station, end_station, time_diff = event
            
            if start_station == startStation and end_station == endStation:
                
                num_events += 1
                avg += time_diff
                
       
        return avg/num_events
        



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
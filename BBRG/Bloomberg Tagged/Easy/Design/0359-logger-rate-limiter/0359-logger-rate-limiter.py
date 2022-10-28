class Logger:
    
    def __init__(self):
        self.unique = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.unique:
            #compute time difference
            time_difference = timestamp - self.unique[message]
            
            if time_difference < 10:
                return False
            else:
                self.unique[message] = timestamp
                return True
        else:
            self.unique[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
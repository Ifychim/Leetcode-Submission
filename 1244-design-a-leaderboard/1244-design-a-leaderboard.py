import heapq
class Leaderboard:
    
    def __init__(self):
        self.leaderboard = {} #map to handle player data
        
    def addScore(self, playerId:int, score:int):
        
        if playerId in self.leaderboard:
            self.leaderboard[playerId] += score
            
        else:
            self.leaderboard[playerId] = score
            
    def reset(self, playerId: int):
        
        del self.leaderboard[playerId]
        
    def top(self, k:int):
        
        res = 0
        heap = []
        tracker = k
        
        #create a max heap
        for val in self.leaderboard.values():
            heapq.heappush(heap, -val)

        while tracker > 0:
            res += heapq.heappop(heap)
            tracker -= 1
        
        return abs(res)
            
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
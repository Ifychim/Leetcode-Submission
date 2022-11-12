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
        
        sorted_leaderboard = sorted(self.leaderboard.items(), key = lambda x: -x[1]) #sort by scores in desc
        
        top_k = sorted_leaderboard[:k]
        
        res = 0
        
        for player,score in top_k:
            res += score
        
        return res
            
        
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
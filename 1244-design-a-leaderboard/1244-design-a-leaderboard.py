class Leaderboard:
    
    def __init__(self) -> object:
        self.players = {} #id:score
    
    def addScore(self, playerId: int, score: int) -> None: 
        
        if playerId in self.players:
            self.players[playerId] += score
            return
        else:
            self.players[playerId] = score
            return
    
    def reset(self, playerId: int) -> None:
        
        if playerId in self.players:
            del self.players[playerId]
            return
        else:
            return
            
    def top(self, k:int) -> int:
        
        sorted_players = sorted(self.players.items(), key =  lambda x: (-x[1]))
    
        top_k = sorted_players[:k]
        
        res = 0

        for data in top_k:

            k, v = data
            res += v
            
       
        return res


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
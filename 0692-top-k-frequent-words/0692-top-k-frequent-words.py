class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq_map = {}
        
        for word in words:
            freq_map[word] = freq_map.get(word,0) + 1
            
        sorted_freq = sorted(freq_map.items(), key = lambda x: (-x[1],x[0]))
        
        res = []
        
        for i in range(0,k):
            res.append(sorted_freq[i][0])
            
        return res
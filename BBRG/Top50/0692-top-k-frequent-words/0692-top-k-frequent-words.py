import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq_map = {}
        
        for word in words:
            freq_map[word] = freq_map.get(word,0) + 1
        
        heap, res = [], []
        
        for key,val in freq_map.items():
            
            heapq.heappush(heap, (-val, ord(key[0]), key))
        
        counter = k
        
        while counter > 0:
            val,ascii_val,word = heapq.heappop(heap)
            res.append(word)

            counter -=1
            
        return res

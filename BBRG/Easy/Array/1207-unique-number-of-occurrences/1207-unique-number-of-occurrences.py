class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq_dict = {}
        unique_frequencies = set()
        
        for num in arr:
            freq_dict[num] = freq_dict.get(num,0) + 1
            
        for num in freq_dict.values():
            
            if num in unique_frequencies:
                return False
            else:
                unique_frequencies.add(num)
            
        
    
        return True
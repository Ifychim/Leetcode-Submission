from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana_map = defaultdict(list)
        
        for word in strs:
            
            temp = ''.join(sorted(word))
            
            
            ana_map[temp].append(word)
      
        
        return ana_map.values()
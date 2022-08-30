from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Create a default dict of all anagrams {key = sorted str of input ; val = [anagrams of key]}

        ana_map = defaultdict(list)
        
        for string in strs:
            sorted_str = ''.join(sorted(string))
            
            if sorted_str in ana_map:
                ana_map[sorted_str].append(string)
            else:
                ana_map[sorted_str].append(string)
        
      
        result = list(ana_map.values())
        
        return result
   
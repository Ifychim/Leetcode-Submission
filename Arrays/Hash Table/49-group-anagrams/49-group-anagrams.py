from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Create a map consisting of {anagram:[list of corresponding anagrams]}
        #The anagram will be the reverse of each word in the input.
        #At each iteration we check to see if we have seen the anagram before and update the map accordingly.

        ana_map = defaultdict(list)
        
        for string in strs:
            sorted_str = ''.join(sorted(string))
            
            if sorted_str in ana_map:
                ana_map[sorted_str].append(string)
            else:
                ana_map[sorted_str].append(string)
        
      
        result = ana_map.values()
        
        return result
   
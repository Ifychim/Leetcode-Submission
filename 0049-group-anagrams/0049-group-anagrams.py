from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #idea is to iterate through string and find if a str is an anagram of another str
        #by having a base anagram, we can compare each string to it.
        ana_map = defaultdict(list)
        
        for str_ in strs:
        
            temp = ''.join(sorted(list(str_)))
            
            
            if temp not in ana_map:
                ana_map[temp].append(str_)
            else:
                ana_map[temp].append(str_)
                
        return ana_map.values()
                
        
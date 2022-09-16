from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #anagarams : [matches] -> aet: ['eat', 'tea', 'ate'].... anagram will be each sorted word 
        
        #create a dictionary consisting of anagrams and their matches
        
        anagram_dict = defaultdict(list)
        
        for word in strs:
            
            temp = ''.join(sorted(word))
            
            if temp in anagram_dict.keys():
                anagram_dict[temp].append(word)
            else:
                anagram_dict[temp] = [word]
        
        #return anagram values
        return anagram_dict.values()
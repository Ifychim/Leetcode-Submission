class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        
        
        freq_map = {}
        result = 0
        stray_odd = False
        for char in s:
            freq_map[char] = 1 + freq_map.get(char,0)
            
        for key,val in freq_map.items():
        
            #if we have an even frequency of a specific letter, add frequency to length
            if val %2 == 0:
                result += val
            elif val %2 != 0:
    #if we have an odd frequency of a specific letter, subtract one from its' frequency & add remainder
                result += freq_map.get(key,0) - 1
                stray_odd = True
        
        #Keep track of stray odd letters by adding one if an odd letter is seen
        
        if stray_odd:
            result += 1
        
        return result
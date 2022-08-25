class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #build a frequency map num:freq
        
        freq_dict = {}
        
        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num,0)
        
        #return true if any freq > 1
        for key, val in freq_dict.items():
            if val > 1:
                return True
        
        #return false if above condition not met
        
        return False
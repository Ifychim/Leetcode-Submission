class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #O(N) time, #O(N) space
        freq_dict = {}
        
        for num in nums:
            
            freq_dict[num] = 1 + freq_dict.get(num, 0)
            
        for key,val in freq_dict.items():
            if val > len(nums)/2:
                return key
        
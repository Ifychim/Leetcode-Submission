class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        num_len = len(nums)
        res = []
        freq_dict = {} #count each number frequency. Return the frequencies that are equal to num_len
        
        for num in nums:
            for n in num:
                freq_dict[n] = freq_dict.get(n,0) + 1
         
        for key,val in freq_dict.items():
            
            if val == num_len:
                res.append(key)
                
        res = sorted(res)
        return res
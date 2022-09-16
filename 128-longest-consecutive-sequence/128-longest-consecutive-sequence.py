class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #use a set to eliminate duplicates
        num_set = set(nums)
       
        result = 0
        
        #check if each number is the start of a consecutive sequence. 
        #start of a sequence = if number behind is not in set of numbers
        
        
        for num in nums:
            
            if num - 1 not in num_set:
                
                longest = 1
                
                while num + longest in num_set:
                    
                    longest += 1
                    
                result = max(result,longest)
            
        return result
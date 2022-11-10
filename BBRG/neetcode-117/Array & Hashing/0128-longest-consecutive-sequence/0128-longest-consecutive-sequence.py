class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        
        #idea is that if curr_num-1 is not in the set then curr can be the beginning of a sequence
        
        #check consecutive numbers from num which are in set and compute length of sequence
        
        result = 0
        
        for num in num_set:
            
            if num-1 not in num_set:
                length = 1
                temp = num
                
                while temp in num_set:
                    temp += 1
                    if temp not in num_set: 
                        break
                    else:
                        length += 1
                result = max(length,result)
                
        return result
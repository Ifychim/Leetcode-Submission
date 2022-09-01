class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums,reverse=True) 
        
        answer_dict = {}
     
        for i in range(0,len(nums)):
            counter = 0
            for j in range(i+1, len(nums)):
                if sorted_nums[j] < sorted_nums[i]:
                    counter += 1
            answer_dict[sorted_nums[i]] = counter 
        
        result = []
        for i in range(0,len(nums)):
            
            if nums[i] in answer_dict.keys():
                result.append(answer_dict[nums[i]])
                
        return result
            
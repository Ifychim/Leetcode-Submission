class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comp_dict = {} #value:compliment
        
        
        for idx,num in enumerate(nums):
            
            compliment = target - num

            if compliment in comp_dict:
                return [nums.index(compliment),idx]
                
            else:
                comp_dict[num] = compliment
                
        print(comp_dict)
                
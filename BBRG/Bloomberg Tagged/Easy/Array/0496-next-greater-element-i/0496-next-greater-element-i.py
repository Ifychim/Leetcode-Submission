class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #for each element(x) in nums1, find index of corresponding element(y) in nums2
        
        #find the next greater element of(y) in nums2, if doesnt exist append -1
        
        result = []
        
        nums1_dict = {} #4:0, 1:1, 2:2
        nums2_dict = {} #1:0, 3:1, 4:2, 2:3
        
        
        for idx, num in enumerate(nums1):
            nums1_dict[num] = idx
            
        for idx, num in enumerate(nums2):
            nums2_dict[num] = idx
            
        for k,v in nums1_dict.items():
            
            if k in nums2_dict:
              
                idx = nums2_dict[k]
                temp = nums2[idx+1:]
                print(k, temp)
                if len(temp) > 0:
                    counter = 0
                    for num in temp:
                        if num > k:
                            result.append(num)
                            counter += 1
                            break
                    if counter == 0:
                        result.append(-1)
                else:
                    result.append(-1)
            
        return result
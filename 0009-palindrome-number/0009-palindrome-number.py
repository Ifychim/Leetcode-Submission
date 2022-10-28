class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num_list = list(str(x))
        print(num_list)
        low = 0
        high = len(num_list)-1
        
        while low <= high:
            
            if num_list[low] != num_list[high]:
                return False
            
            low += 1
            high -= 1
            
        return True
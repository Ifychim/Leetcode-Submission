class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(0,len(matrix)):
            
            for col in range(0,len(matrix[0])):
                
                first_col_val = matrix[row][0]
                last_col_val = matrix[row][len(matrix[0])-1]
                
                if target >= first_col_val and target <= last_col_val:
                    #perform binary search
                    print(matrix[row])
                    if self.binarySearch(matrix[row], target):
                        return True
                    else:
                        return False
                else:
                    continue
                    
        return False
    
    
    def binarySearch(self, row, target) -> bool:
        
        low = 0
        high = len(row)-1
        
        while low <= high:
            
            mid = (high + low) // 2
            
            if row[mid] == target:
                return True
            
            if row[mid] < target:
                low = mid + 1
                
            elif row[mid] > target:
                high = mid -1
                
        return False
            
            
            
            
            
            
            
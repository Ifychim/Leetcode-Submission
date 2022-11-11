class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        result = 0
        
        for row in range(0,len(grid)):
            
            for col in range(0,len(grid[0])):
                
                if grid[row][col] == "0": continue
                
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    result += 1
                    
        return result
    
    
    def dfs(self, grid, row, col):
        
        #base cases -> out of bounds length wise or width wise, or we are at a visited island/water (2)
        if row >= len(grid) or row < 0: return
        if col >= len(grid[0]) or col < 0: return
        if grid[row][col] == "2" or grid[row][col] == "0": return
        
        #mark island as visited then call dfs on all 4 sides
        grid[row][col] = "2"
        
        self.dfs(grid, row-1, col)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col-1)
        self.dfs(grid, row, col+1)
        
        
        
        
        
        
        
        
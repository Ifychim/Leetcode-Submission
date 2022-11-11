class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #basically number of island but we need to compute #island visited on an island
        
        max_area = 0
        
        for row in range(0,len(grid)):
            
            for col in range(0,len(grid[0])):
                
                if grid[row][col] == 0: continue
                    
                if grid[row][col] == 1:
                    max_area = max(self.dfs(grid, row, col), max_area)
                    
        return max_area
    
    
    def dfs(self, grid,row,col):
        
        #edge cases -> boundaries of grid, hit water, or visit a visited node
        
        if row < 0 or row >= len(grid): return 0
        if col < 0 or col >= len(grid[0]): return 0
        if grid[row][col] == 2 or grid[row][col] == 0: return 0
        
        
        #mark node as visited then calculate max_area per successful dfs call (add one for curr island)
        grid[row][col] = 2
        
        
        #call dfs
        return (1 + self.dfs(grid, row-1, col) +
                    self.dfs(grid, row+1, col) +
                    self.dfs(grid, row, col-1) +
                    self.dfs(grid, row, col+1))

        
        
        
        
        
        
        
        
        
        
        
        
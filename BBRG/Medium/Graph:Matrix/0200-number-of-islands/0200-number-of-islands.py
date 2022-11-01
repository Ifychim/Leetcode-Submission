class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0
        
        for row in range(0,len(grid)):
            
            for col in range(0,len(grid[0])):
            
                if grid[row][col] == "1":
                    self.dfs(row, col, grid)
                    num_islands += 1
                         
        return num_islands
                
        
    def dfs(self, row, col, grid):
        #edge cases (out of bounds on right or left)
        if row >= len(grid) or col >= len(grid[0]): return
        if row < 0 or col < 0: return
        
        #if we have visited land already or we hit water
        if grid[row][col] == "0": return
        if grid[row][col] == "2": return
        
        
        #mark cell as visited
        grid[row][col] = "2"
        
        #dfs to traverse all possible islands
        self.dfs(row,col-1,grid)
        self.dfs(row,col+1,grid)
        self.dfs(row-1,col,grid)
        self.dfs(row+1,col,grid)        
        
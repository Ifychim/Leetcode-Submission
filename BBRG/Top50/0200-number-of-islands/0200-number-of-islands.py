class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        result = 0
        
        for row in range(0,len(grid)):
            
            for col in range(0,len(grid[0])):
                
                if grid[row][col] == "1":
                    
                    self.dfs(grid, row, col)
                    result += 1
        
        return result
    
    def dfs(self, grid, row, col):
        
        #out of bounds either vertically or horizontally, if we hit water, or if we visit an explored node
        if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1: return
        elif grid[row][col] == "0": return
        elif grid[row][col] == "V": return
        
        grid[row][col] = "V"
        
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)
        
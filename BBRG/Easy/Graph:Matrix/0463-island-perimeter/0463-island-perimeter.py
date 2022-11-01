class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        Idea is to use dfs on every cell of the grid
        Base case(s) 1 - If we reach edge of grid / out of bounds
                     2 - If we dfs in a particular direction lands us on water(0)
                     3 - If we re-visit an already visted island
        Keep track of visited islands by marking them as '2'
        '''

        
        for row in range(0,len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col]:
                    return self.dfs(row, col, grid)
        
    def dfs(self, row, col , grid):
        
        #Base Case(s)
    
        #Out-Of-Bounds
        if row >= len(grid) or col >= len(grid[0]): return 1
        elif row < 0 or col < 0 : return 1
        
        #Reached water or re-visiting an island
        elif grid[row][col] == 0: return 1
        elif grid[row][col] == 2: return 0
        
        #mark island as visited
        grid[row][col] = 2
        
        #dfs in all 4 directions to compute perimeter (left,right,up_down)
        perimeter = 0
        perimeter += self.dfs(row,col-1,grid)
        perimeter += self.dfs(row,col+1,grid)
        perimeter += self.dfs(row-1,col,grid)
        perimeter += self.dfs(row+1,col,grid)
        
        return perimeter
        
        
        
        
        
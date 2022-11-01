class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        Idea is to use dfs on every cell of the grid
        Base case(s) 1 - If we reach edge of grid / out of bounds
                     2 - If we dfs in a particular direction lands us on water(0)
                     3 - If we visit an already visted island
        Keep track of visited nodes and return 1 on base cases
        '''
        
        visited_islands = set() #set of unique islands we have visted via dfs
        
        for row in range(0,len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col]:
                    return self.dfs(row, col, grid, visited_islands)
        
    
    def dfs(self, row, col , grid, visited_islands):
        
        #Base Case(s)
        
        #Out-Of-Bounds
        if row >= len(grid) or col >= len(grid[0]): return 1
        elif row < 0 or col < 0 : return 1
        #Reached water
        elif grid[row][col] == 0: return 1
        elif (row,col) in visited_islands: return 0
        
        visited_islands.add((row,col))
        
        #dfs in all 4 directions to compute perimeter (left,right,up_down)
        perimeter = 0
        perimeter += self.dfs(row,col-1,grid, visited_islands)
        perimeter += self.dfs(row,col+1,grid, visited_islands)
        perimeter += self.dfs(row-1,col,grid, visited_islands)
        perimeter += self.dfs(row+1,col,grid, visited_islands)
        
        return perimeter
        
        
        
        
        
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#create unique hash-sets for each row,col & subgrid in the grid to make sure there arent any duplicates
        
        row_set = defaultdict(set) #key = row_idx, val = set()
        col_set = defaultdict(set) #key = col_idx, val = set()
        sub_grid_set = defaultdict(set) #key = (row_idx/3, col_idx/3) val = set(duplicate)
        
        
        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                
                #if we encounter an empty cell, skip it
                if board[row][col] == ".": continue
                
                
                #checking if duplicates exist in row, columns and sub_grids
                if (board[row][col] in row_set[row] 
                    or board[row][col] in col_set[col] 
                    or board[row][col] in sub_grid_set[(row//3,col//3)] ):
                    return False
                
                #adding cells to corresponding sets
                row_set[row].add(board[row][col])
                col_set[col].add(board[row][col])
                sub_grid_set[(row//3,col//3)].add(board[row][col])

        
        return True
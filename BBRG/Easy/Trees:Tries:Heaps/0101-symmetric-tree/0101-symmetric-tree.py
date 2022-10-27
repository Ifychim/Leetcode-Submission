# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root == None: return False
        
        #bfs to get level elements
        q = deque()
        q.append(root)
        
        levels = []
        
        while q:
            
            level = []
            level_len = len(q)
            
            for i in range(level_len):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
        
            if level:
                levels.append(level)
        
        print(levels)
        #split levels in half, compare each half to each other.
        for i in range(1,len(levels)):
            if self.split_compare(levels[i]) == False:
                return False
        
        return True
    
    def split_compare(self, arr) -> bool:
        half = int(len(arr)/2)
        
        first_half = arr[:half]
        second_half = arr[half:]
        
        if len(first_half) != len(second_half): return False
        
        low = 0
        high = len(arr)-1
        
        while low <= high:
            if arr[low] != arr[high]:
                return False
            low += 1
            high -= 1
            
        return True
        
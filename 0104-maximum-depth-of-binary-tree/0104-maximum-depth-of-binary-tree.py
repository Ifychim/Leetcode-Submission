# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        
        result = [] #hold all nodes in tree. result[i] indicates the nodes on level i
        
        while q:
            
            level = []
            level_length = len(q)
            
            for _ in range(level_length):
                
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                result.append(level)
                    
        return len(result)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        
        
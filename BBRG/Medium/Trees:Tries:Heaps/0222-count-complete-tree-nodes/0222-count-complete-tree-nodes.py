# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        
        q = deque()
        num_nodes = 0
        levels = []
        
        q.append(root)
        
        while q:
            
            level = []
            level_len = len(q)
            
            for _ in range(level_len):
                
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                levels.append(level)
                
        for level in levels:
            num_nodes += len(level)
            
        return num_nodes
                
            
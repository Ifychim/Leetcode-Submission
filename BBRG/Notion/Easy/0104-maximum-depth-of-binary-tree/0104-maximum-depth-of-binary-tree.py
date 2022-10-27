# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #bfs count levels
        q = deque()
        q.append(root)
        levels = []
        
        while q:
            level_len = len(q)
            level = []
            for _ in range(level_len):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                levels.append(level)
    
        return len(levels)
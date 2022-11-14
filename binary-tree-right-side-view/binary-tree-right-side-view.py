# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs, store last element of each level to result
        
        q = deque()
        q.append(root)
        
        levels = []
        result = []
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
                
                
        for i in range(len(levels)):
            result.append(levels[i][-1])
            
        return result
                
                
                
                
                
                
                
                
                
                
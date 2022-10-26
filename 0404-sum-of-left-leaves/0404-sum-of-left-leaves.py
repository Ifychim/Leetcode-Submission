# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        #typical bfs, compute running sum of nodes which dont have left children
        
        q = deque()
        q.append(root)
        result = 0

        
        while q:
            level_len = len(q)
            
            for i in range(level_len):
                
                node = q.popleft()
                
                if node:
                    
                    if node.left:
                        q.append(node.left)
                        if node.left.left == None and node.left.right == None:
                            result += node.left.val
                            
    
                    if node.right:
                        q.append(node.right)

                           
        return result
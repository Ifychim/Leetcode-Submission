# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        deq = deque()
        deq.append(root)
        
        result = []
        flag = True #true = left -> right, false = right -> left
        
        while deq:
            #traverse and build the current level of the tree we are on
            level_len = len(deq)
            level = deque()
            
            for _ in range(level_len):
    
                node = deq.popleft()
                if node:
                    deq.append(node.left)
                    deq.append(node.right)
                    if flag:
                        #left to right
                        level.append(node.val)
                    else:
                        #right to left
                        level.appendleft(node.val) 
                        
            flag = not flag
            if level:
                result.append(level)
                
                
        return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
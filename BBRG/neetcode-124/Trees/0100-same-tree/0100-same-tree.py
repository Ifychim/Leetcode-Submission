# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #pre-order dfs
        
        #base-cases
        if p == None and q == None: return True
        if p != None and q == None: return False
        if p == None and q != None: return False
        if p.val != q.val: return False
        
        return(self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
        
        '''
        sol'n 2
        
        #bfs with two queues
        
        p_deque, q_deque = deque(), deque()
        p_deque.append(p)
        q_deque.append(q)
     
        
        while p_deque and q_deque:
            
            p_level = len(p_deque)
            q_level = len(q_deque)
            
            if p_level != q_level: return False
            
            for _ in range(p_level):
                
                p_node = p_deque.popleft()
                q_node = q_deque.popleft()
            
                if p_node == None and q_node != None: return False
                if p_node != None and q_node == None: return False
                
                
                if p_node and q_node:
                    if p_node.val != q_node.val: return False
                    p_deque.append(p_node.left)
                    p_deque.append(p_node.right)
                    q_deque.append(q_node.left)
                    q_deque.append(q_node.right)

        return True
         '''       
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
        
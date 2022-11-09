# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorder = [] #left-root-right
        
        def dfs(root):
            if root == None:
                return None
            
            dfs(root.left)
            
            inorder.append(root.val)
            
            dfs(root.right)
            
        
        dfs(root)
        
        result = inorder[:k][-1]#1,2,3,4
        return result
        
            
        
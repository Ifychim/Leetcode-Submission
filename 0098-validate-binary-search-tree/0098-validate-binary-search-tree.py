# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        min_ = -float('inf')
        max_ = float('inf')
        
        
        
        def dfs(root, min_bounds, max_bounds):
            
            if root == None:
                return True
            
            if not (root.val < max_bounds and root.val > min_bounds):
                return False
            
            #post order
            return(dfs(root.left, min_bounds, root.val) and
            dfs(root.right, root.val, max_bounds))
            
        return dfs(root, min_, max_)
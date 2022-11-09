# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower_bound = -float('inf')
        upper_bound = float('inf')
        def dfs(root,left_bound,right_bound):
            
            if root == None:
                return True
            #check if curr val is between boundaries
            if not (root.val < right_bound and root.val > left_bound):
                return False

            #pre-order -> left, right, root. Check if left subtree is valid, then right subtree
            #LST is upper bounded by root val, RST is lower bounded by root val -> root.val = parent
            return(dfs(root.left, left_bound, root.val) and
            dfs(root.right, root.val, right_bound))
            
        return dfs(root, lower_bound, upper_bound)

            
            
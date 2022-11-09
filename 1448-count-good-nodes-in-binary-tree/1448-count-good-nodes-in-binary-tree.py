# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = [0] #root is always a good node

        #pre-order dfs (root-left-right)
        def dfs(root, max_node):
            
            if root == None:
                return None
            
            #check if curr_node val is greater than or equal max val seen on path.
            #if it is, increment count
            if root.val >= max_node:
                res[0] += 1
                max_node = root.val
                
            #find all good nodes in left sub_tree and right sub_tree recursively    
            dfs(root.left, max_node)
            dfs(root.right, max_node)
            
        dfs(root,root.val)
        
        return res[0]
        
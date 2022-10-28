# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        
        self.dfs(root,stack)
        
        return stack
        
    def dfs(self, root, stack):
        
        if root == None: return []
        
        self.dfs(root.left, stack)#left
        
        self.dfs(root.right, stack)#right
        
        stack.append(root.val)#root
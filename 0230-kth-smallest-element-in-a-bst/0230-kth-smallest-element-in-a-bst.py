# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        elements = []
        def dfs(root):
            if root == None: return
            #inorder = left, root, right
            
            dfs(root.left)
            
            elements.append(root.val)
            
            dfs(root.right)
        
        dfs(root)
        result = elements[k-1]
        return result
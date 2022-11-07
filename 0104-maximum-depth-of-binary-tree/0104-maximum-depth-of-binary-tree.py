# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        left_tree = self.maxDepth(root.left)
        right_tree = self.maxDepth(root.right)
        
        return 1 + max(left_tree, right_tree)
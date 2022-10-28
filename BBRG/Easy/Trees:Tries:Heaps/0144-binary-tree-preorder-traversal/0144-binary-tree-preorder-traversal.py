# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        self.preOrder(root, result)
        
        return result
        
    def preOrder(self, root, res):
        
        if root == None:
            return []
        
        res.append(root.val) #root (explore)
        
        self.preOrder(root.left, res) #left (traverse)
    
        self.preOrder(root.right, res) #right(traverse)
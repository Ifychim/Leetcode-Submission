"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        node_map = {} #used to map old node to copy as we use dfs to traverse
        
        def dfs(node):
            if node == None:
                return
            
            if node in node_map:
                return node_map[node]
            
            copy = Node(val=node.val)
            node_map[node] = copy
            
            #make copy of every neighbor and append to newly created node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
        
        deep_copy = dfs(node)
        return deep_copy
            
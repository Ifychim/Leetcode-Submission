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
        
        #idea is to use pre-order dfs to make a deep copy of each node and its neighbors. 
        #using a map to map old node to the new copy node handles the undirected aspect of the graph.
        
        node_map = {} #used to map old node to copy as we use dfs to traverse
        
        def dfs(node):
            if node == None:
                return
            
            #if copy exists, return the copy
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
            
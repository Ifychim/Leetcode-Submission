from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
        source = [0]
        target = len(graph)-1
        
        result = []
        
        #start of with source in queue
        queue = deque()
        queue.append(source)
        
        
        #while we have nodes to explore, we pop from queue and check if last element is equal to target
        while queue:
            idx = 0
            
            path = queue.popleft()
           
            if path[-1] == target:
                result.append(path)
            else:
                
                for neighbor in graph[path[-1]]:
                    queue.append(path + [neighbor])
    
                
        return result  
            
        
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        #we need to kick bfs off with a queue that is initialized with the source
        
        source = 0
        target = len(graph)-1
        
        queue = deque()
        queue.append([source])
        
        result = []

#if the last element in the queue is equal to the target, we can append the path thus far to result else,
#we need to traverse all the neighbors of our current node and add all possible paths to our queue

        while queue:
            
            path = queue.popleft()
            last_element = path[-1]
            
            if last_element == target:
                result.append(path)
            else:
                for neighbor in graph[last_element]:
                    #take current path and add neighbor to it
                    queue.append(path + [neighbor])
                    
                    
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            cityA, cityB = paths[0]
            return cityB
        #create a map of paths {key = cityA, value = cityB}
        routes = {}
        
        for path in paths:
            cityA, cityB = path
            routes[cityA] = cityB
            
        #iterate through the paths and if a city(a/b) does not have a key, 
        #then we know that city does not have a destination city.
        for path in paths:
            cityA, cityB = path
    
            if cityB not in routes.keys():
                return cityB
        
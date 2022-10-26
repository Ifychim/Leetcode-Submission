class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        year_populations = {}
        logs = sorted(logs)

        for log in logs:
            
            birth_year , death_year = log
            
            year_populations[birth_year] = year_populations.get(birth_year, 0) + 1
            
        for log in logs:
            
            birth_year , death_year = log
            
            for i in range(birth_year+1, death_year):
                if i in year_populations:
                    year_populations[i] += 1
        
        result = sorted(year_populations.items(), key = lambda x: -x[1])
        print(result)
        return result[0][0]
        
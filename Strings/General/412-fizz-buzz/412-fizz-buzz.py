class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        
        for i in range(1, n+1):
            
            #if i is divisible by 3 & 5 -> FizzBuzz
            if i % 5 == 0 and i % 3 == 0:
                answer.append("FizzBuzz")
                
            #if i is divisible by 3 -> Fizz
            elif i % 3 == 0:
                answer.append("Fizz")
            #if i is divisible by  5 -> Buzz
            elif i % 5 == 0:
                answer.append("Buzz")
            #else -> i
            else:
                answer.append("{}".format(i))
            
        return answer
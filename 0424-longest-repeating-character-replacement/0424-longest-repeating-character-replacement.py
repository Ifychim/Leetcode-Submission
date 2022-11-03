class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
#brute force would be to find every substring, and see if we can perform K substitutions
#we can perform K substitutions if a substring is valid -> substrlen - mostfrequentchar <= k

        alphabet_count = {} #to count most frequent element in our substr
        
        low = 0 #sliding window
    
        
        result = 0
        length = 0
        
        for high in range(len(s)):
            
            alphabet_count[s[high]] = alphabet_count.get(s[high],0) + 1
            length += 1
            most_freq = max(alphabet_count.values())
            
            if length - most_freq <= k:
                high += 1
            else:
                while length - most_freq > k:
                    print(low, high, result, length)
                    alphabet_count[s[low]] -= 1
                    low += 1
                    length -= 1

                
            result = max(result, length)
            
        return result
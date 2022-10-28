class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        result = 0
        
        for char in letters:
            
            if ord(char) > ord(target):
                return char
        
        return letters[0]
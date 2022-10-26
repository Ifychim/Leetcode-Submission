class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        #intuition -> we know there are 26 unique characters in alphabet
        alphabet = set()
        
        for char in sentence:
            
            #add only chars from a-z to alphabet
            if char.isalpha():
                alphabet.add(char)
            
        
        if len(alphabet) == 26:
            return True
        else:
            return False
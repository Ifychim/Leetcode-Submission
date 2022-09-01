class Solution:
    def interpret(self, command: str) -> str:
        #one line solution -> return command.replace("()", "o").replace("(al)","al")
        
        #intricate solution
        #build a mapping for the alphabet
        
        alphabet = {"G": "G", 
                    "()":"o", 
                    "(al)":"al"}
        result = ""
        temp = ""
        #iterare through command concatenating every letter found in alphabet
        for char in command:
            temp += char
            
            if temp in alphabet:
                result += alphabet[temp]
                temp = ""
                
        return result
        
        
        
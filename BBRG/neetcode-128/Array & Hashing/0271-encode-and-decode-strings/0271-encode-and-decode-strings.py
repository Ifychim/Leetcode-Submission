class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        
        for word in strs:
            
            word_len = len(word)
            unique_delimeter = "#"
            combined_delimeter = str(word_len) + unique_delimeter
            
            encoded_str += combined_delimeter
            encoded_str += word
            
        return encoded_str
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        encoded_str_list = []
        i = 0
        
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
 
            encoded_str_list.append(s[j+1:j+1+length])
            
            i = j+1+length
            
        return encoded_str_list


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
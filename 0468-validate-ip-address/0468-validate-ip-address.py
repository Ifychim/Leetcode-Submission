class Solution:
    def validIPAddress(self, queryIP: str) -> str:
 
        ipv4, ipv6 = False, False
        
        if "." in queryIP:
            #pre-processing
            for digit in queryIP:
                if digit == '.': continue
                    
                if not digit.isnumeric():
                    return "Neither"
    
            ipv4 = self.validate_ipv4(queryIP)
        
        elif ":" in queryIP:
            #pre-processing
            for digit in queryIP:
                if digit.isupper() and ord(digit) > 70:
                    return "Neither"
                elif digit.islower() and ord(digit) > 102:
                    return "Neither"
                
            ipv6 = self.validate_ipv6(queryIP)
        
        
        if ipv4:
            return "IPv4"
        elif ipv6:
            return "IPv6"
        else:
            return "Neither"
        
    
    def validate_ipv4(self, ip_address:str) -> bool:
        
        ip_address = ip_address.split('.')
    
        if '' in ip_address: return False
        elif len(ip_address) != 4: return False
        
        for digits in ip_address:
            
            first_digit = int(digits[0])
            entire_digit = int(digits)
            entire_digit_str = str(digits)
            
            if first_digit == 0 and len(entire_digit_str) > 1:
                return False
            if entire_digit < 0 or entire_digit > 255:
                return False
            
        return True
    
    
    def validate_ipv6(self, ip_address:str) -> bool:
        
        ip_address = ip_address.split(':')
        
        if '' in ip_address: return False
        elif len(ip_address) != 8: return False
        
        for digits in ip_address:
            
            entire_digit = str(digits)
            
            if len(entire_digit) < 1 or len(entire_digit) > 4:
                
                return False
            
        return True
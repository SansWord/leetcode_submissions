class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            return self.maskEmail(s)
        else:
            return self.maskPhone(s)
    
    def maskEmail(self, s: str) -> str:
        name, domain = s.lower().split("@")
        masked_name = f"{name[0]}*****{name[-1]}"
        return f"{masked_name}@{domain}"
    
    def maskPhone(self, s: str) -> str:
        digits = "0123456789"
        number = []
        for c in s:
            if c in digits:
                number.append(c)
        if len(number) == 10:
            return "***-***-" + "".join(number[-4:])
        else:
            return "+"+ "*" * (len(number)-10) +"-***-***-" + "".join(number[-4:])
        

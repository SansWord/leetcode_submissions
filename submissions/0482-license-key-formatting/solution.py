class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        val = "".join(s.split("-")).upper()
        size = len(val)
        first = size % k
        if first == 0:
            first = k
        
        result = []
        result.append(val[:first])
        start = first
        while start < size:
            result.append(val[start:start+k])
            start += k

        return "-".join(result)
        

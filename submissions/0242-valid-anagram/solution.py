class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrence = defaultdict(int)
        for c in s:
            occurrence[c] += 1
        
        for c in t:
            if not c in occurrence or occurrence[c] == 0:
                return False
            occurrence[c] -= 1
        
        return sum(occurrence.values()) == 0

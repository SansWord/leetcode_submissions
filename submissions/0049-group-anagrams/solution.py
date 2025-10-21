class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            key = "".join(sorted(list(word)))
            group[key].append(word)
        
        return list(group.values())
        

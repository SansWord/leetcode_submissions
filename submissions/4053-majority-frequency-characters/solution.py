class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        fq = defaultdict(int)
        for c in s:
            fq[c] += 1

        fgp = defaultdict(lambda: [])

        for c, f in fq.items():
            fgp[f].append(c)
        
        maxG = None
        maxSize = 0
        for gKey in sorted(fgp.keys())[::-1]:
            group = fgp[gKey]
            if len(group) > maxSize:
                maxSize = len(group)
                maxG = group


        return "".join(maxG)
        

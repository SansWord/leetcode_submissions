class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        vowel_feq = defaultdict(int)
        consonant_feq = defaultdict(int)

        for c in s:
            if c in vowels:
                vowel_feq[c] += 1
            else:
                consonant_feq[c] += 1

        max_vowel_feq = 0
        for key, feq in vowel_feq.items():
            if feq > max_vowel_feq:
                max_vowel_feq = feq
        
        max_consonant_feq = 0
        for key, feq in consonant_feq.items():
            if feq > max_consonant_feq:
                max_consonant_feq = feq
        
        return max_consonant_feq + max_vowel_feq


        

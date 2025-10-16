class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        mapping = {}
        mappedWords = set()
        for i in range(len(pattern)):
            c = pattern[i]
            word = words[i]
            if c not in mapping:
                if word in mappedWords:
                    return False
                mapping[c] = word
                mappedWords.add(word)
            else:
                if word != mapping[c]:
                    return False

        return True

        

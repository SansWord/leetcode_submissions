class Solution:
    def generateTag(self, caption: str) -> str:
        words = [word for word in caption.lower().split(" ") if len(word) != 0]
        LEN = len(words)
        if LEN == 0:
            return "#"

        tagParts = [None for i in range(LEN)]

        tagParts[0] = words[0]

        for i in range(1, LEN):
            word = words[i]
            if len(word) == 1:
                tagParts[i] = word.upper()
            else:
                tagParts[i] = word[0].upper() + word[1:]

        return ("#" + "".join(tagParts))[:100]

        

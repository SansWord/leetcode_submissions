class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # construct chr_to_row dict
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        chr_to_row = {}
        for idx, row in enumerate(rows):
            for char in row:
                chr_to_row[char] = idx

        def valid(word):
            row = chr_to_row[word[0]]
            for char in word[1:]:
                curr_row = chr_to_row[char]
                if row != curr_row:
                    return False

            return True


        return [word for word in words if valid(word.lower())]


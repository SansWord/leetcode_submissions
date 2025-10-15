class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # words can have duplicates

        sLen = len(s)
        wordsLen = len(words)
        wordLen = len(words[0])
        wordPos = defaultdict(list)
        for i, word in enumerate(words):
            wordPos[word].append(i)
        
        expectedLen = wordLen * wordsLen
        
        res = []
        for i in range(wordLen):
            l = 0
            correntFoundWords = defaultdict(int)
            correntFoundWordsPos = deque()
            for j in range(i, sLen-wordLen+1, wordLen):
                currWord = s[j:j+wordLen]
                if not currWord in wordPos:
                    correntFoundWords = defaultdict(int)
                    correntFoundWordsPos = deque()
                else:
                    if len(correntFoundWords) == 0:
                        l = j

                    idxes = wordPos[currWord]
                    foundNum = correntFoundWords[currWord]
                    idx = idxes[foundNum]
                    correntFoundWords[currWord] = (foundNum + 1) % len(idxes)

                    while idx in correntFoundWordsPos:
                        correntFoundWordsPos.popleft()
                        l+=wordLen
                    
                    correntFoundWordsPos.append(idx)

                    if len(correntFoundWordsPos) == wordsLen:
                        res.append(l)


        return res


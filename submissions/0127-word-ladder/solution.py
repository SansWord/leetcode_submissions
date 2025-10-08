import queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0

        if not beginWord in wordList:
            wordList.append(beginWord)

        wordListLength = len(wordList)
        beginIdx = wordList.index(beginWord)
        endIdx = wordList.index(endWord)

        
        connected_map = [ [] for i in range(wordListLength)]
        # construct relationship between words
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.is_connected(wordList[i], wordList[j]):
                    connected_map[i].append(j)
                    connected_map[j].append(i)

        # find shortest path from beginIdx to endIdx
        seen = [False for i in range(wordListLength)]
        q = queue.Queue()
        level = 1

        seen[beginIdx] = True
        q.put(beginIdx)
        

        while not q.empty():
            for i in range(q.qsize()):
                curr = q.get()
                if curr == endIdx:
                    return level    

                for adj in connected_map[curr]:
                    if not seen[adj]:
                        seen[adj] = True
                        q.put(adj)
            level += 1
                    

        return 0

    def is_connected(self, word1, word2) -> bool:
        found = False
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                if found:
                    return False
                found = True
        return True
        

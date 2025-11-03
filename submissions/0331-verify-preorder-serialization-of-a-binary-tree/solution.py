class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tokens = deque(preorder.split(","))

        return self.extractOneTree(tokens) and len(tokens) == 0
    
    def extractOneTree(self, tokens) -> bool:

        if len(tokens) == 0:
            return False

        curr = tokens.popleft()
        if curr == "#":
            return True
        else:
            return self.extractOneTree(tokens) and self.extractOneTree(tokens)

        
        

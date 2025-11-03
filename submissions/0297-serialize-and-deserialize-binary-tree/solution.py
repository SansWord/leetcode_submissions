# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right) 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tokens = deque(data.split(","))

        return self.parse(tokens)

    def parse(self, tokens): 
        curr = tokens.popleft()
        if curr == "#":
            return None
        
        node = TreeNode(int(curr))
        node.left = self.parse(tokens)
        node.right = self.parse(tokens)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

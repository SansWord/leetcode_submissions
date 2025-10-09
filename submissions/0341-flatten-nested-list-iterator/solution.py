# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.cleaned = False
        
    
    def next(self) -> int:
        return self.pop(self.nestedList)
        
    
    def hasNext(self) -> bool:
        if not self.cleaned:
            self.tidyList(self.nestedList)
            self.cleaned = True
        return len(self.nestedList) != 0

    def pop(self, nestedList: [NestedInteger])-> int:
        nestedInteger = nestedList[0]
        if nestedInteger.isInteger():
            nestedList.pop(0)
            return nestedInteger.getInteger()
        else:
            result = self.pop(nestedInteger.getList())
            if len(nestedInteger.getList()) == 0:
                nestedList.pop(0)
            return result

    def tidyList(self, nestedIntegerList: [NestedInteger]) -> None:
        idxToRemove = []

        for i in range(len(nestedIntegerList)):
            node = nestedIntegerList[i]
            if not node.isInteger():
                self.tidyList(node.getList())
                if len(node.getList()) == 0:
                    idxToRemove.append(i)

        for i in range(len(idxToRemove)):
            nestedIntegerList.pop(idxToRemove.pop())


        return
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

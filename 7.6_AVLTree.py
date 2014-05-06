
#-----------------------------------------------------------------------------
# Define a BalancedBinarySearchTree class that inherits from BST class
# the height of a Balanced BST is 1.44logn

class AVLTree(BinarySearchTree):

    def __init__(self):
        super(AVLTree, self).__init__()

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                newNode = TreeNode(key, val, parent = currentNode)
                currentNode.leftChild = newNode
                self.updateBalFac(newNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                newNode = TreeNode(key, val, parent = currentNode)
                currentNode.rightChild = newNode
                self.updateBalFac(newNode)

    def updateBalFac(self, currentNode):
        if currentNode.balanceFactor not in [-1, 0, 1]:
            self.rebalance(currentNode)
            return
        if currentNode.parent != None:
            if currentNode.isLeftChild():
                currentNode.parent.balanceFactor += 1
            elif currentNode.isRightChild():
                currentNode.parent.balanceFactor -= 1
            if currentNode.parent.balanceFactor != 0:
                self.updateBalFac(currentNode.parent)

    def rebalance(self, currentNode):
        if currentNode.balanceFactor < 0: # right-heavy
            if currentNode.rightChild.balanceFactor > 0: # if rightChild is left-heavy
                self.rotateRight(currentNode.rightChild)
                self.rotateLeft(currentNode)
            else:
                self.rotateLeft(currentNode)
        else: # left-heavy
            if currentNode.leftChild.balanceFactor < 0: # if leftChild is right-heavy
                self.rotateLeft(currentNode.leftChild)
                self.rotateRight(currentNode)
            else:
                self.rotateRight(currentNode)
            
    def rotateLeft(self, oldRoot):
        newRoot = oldRoot.rightChild
        oldRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = oldRoot
        newRoot.parent = oldRoot.parent
        if oldRoot.isRoot():
            self.root = newRoot
        else:
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        newRoot.leftChild = oldRoot
        oldRoot.parent = newRoot
        oldRoot.balanceFactor = oldRoot.balanceFactor + 1 - min(0, newRoot.balanceFactor)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(0, oldRoot.balanceFactor)

    def rotateRight(self, oldRoot):
        newRoot = oldRoot.leftChild
        oldRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = oldRoot
        newRoot.parent = oldRoot.parent
        if oldRoot.isRoot():
            self.root = newRoot
        else:
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        newRoot.rightChild = oldRoot
        oldRoot.parent = newRoot
        oldRoot.balanceFactor = oldRoot.balanceFactor - 1 + max(0, newRoot.balanceFactor)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 - min(0, oldRoot.balanceFactor)

myAVL = AVLTree()
myAVL[20] = 'a'
myAVL[9] = 'b'
myAVL[21] = 'c'
myAVL[23] = 'd'
myAVL[22] = 'e'
print myAVL[9]
print 12 in myAVL
for tree1 in myAVL:
    print tree1

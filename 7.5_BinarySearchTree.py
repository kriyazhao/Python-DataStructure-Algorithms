
#-----------------------------------------------------------------------------
# Define a TreeNode class and a BinarySearchTree class

class TreeNode:

    def __init__(self, key, val, left = None, right = None, parent = None):
        self.key = key
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent # designed for "del" operator
        self.balanceFactor = 0 # designed for AVL tree

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, left, right):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self != None:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        if self.size == 0:
            newNode = TreeNode(key, val)
            self.root = newNode
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, currentNode): # a private function
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                newNode = TreeNode(key, val)
                currentNode.leftChild = newNode
                newNode.parent = currentNode

        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                newNode = TreeNode(key, val)
                currentNode.rightChild = newNode
                newNode.parent = currentNode

    def get(self, key):
        if self.root != None:
            result = self._get(key, self.root)
            if result != None:
                return result.value
            else:
                return None
            
    def _get(self, key, currentNode): # a private function
        if not currentNode:
            return None
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            return self._get(key, currentNode.rightChild)
        else:
            return currentNode
        
    def delete(self, key):
        if self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        elif self.size > 1:
            delNode = self._get(key, self.root)
            if delNode == None:
                raise KeyError('the key is not in the BST!')
            else:
                self.remove(delNode)
                self.size -= 1
        else:
            raise KeyError('the key is not in the BST!')

    def remove(self, delNode):
        if delNode.isLeaf(): # delNode is a leaf node
            if delNode == delNode.parent.leftChild:
                delNode.parent.leftChild = None
            else:
                delNode.parent.rightChild = None
        elif delNode.hasBothChildren(): # delNode has both children
            successor = delNode.findSuccessor()
            self.remove(successor)
            delNode.key = successor.key
            delNode.value = successor.value
        else: # delNode has only one child
            if delNode.hasLeftChild():
                if delNode.isLeftChild():
                    delNode.leftChild.parent = delNode.parent
                    delNode.parent.leftChild = delNode.leftChild 
                elif delNode.isRightChild():
                    delNode.leftChild.parent = delNode.parent
                    delNode.parent.rightChild = delNode.leftChild 
                else: # if delNode is the root node
                    delNode.replaceNodeData(delNode.leftChild.key,
                                            delNode.leftChild.value,
                                            delNode.leftChild.leftChild,
                                            delNode.leftChild.rightChild)
            else:
                if delNode.isLeftChild():
                    delNode.rightChild.parent = delNode.parent
                    delNode.parent.leftChild = delNode.rightChild 
                elif delNode.isRightChild():
                    delNode.rightChild.parent = delNode.parent
                    delNode.parent.rightChild = delNode.rightChild 
                else:
                    delNode.replaceNodeData(delNode.rightChild.key,
                                            delNode.rightChild.value,
                                            delNode.rightChild.leftChild,
                                            delNode.rightChild.rightChild)

    def findSuccessor(self):
        currentNode = self.rightChild
        while currentNode.hasLeftChild():
            currentNode = currentNode.leftChild
        return currentNode
    
    def __setitem__(self, key, val):
        self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)
        
    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        self.length()
        
    def length(self):
        return self.size

    def __contains__(self, key):
        if self._get(key, self.root) == None:
            return False
        else:
            return True
    
    def __iter__(self):
        return self.root.__iter__()
    
myBST = BinarySearchTree()
myBST[20] = 'a'
myBST[5] = 'b'
myBST[21] = 'c'
myBST[3] = 'd'
myBST[10] = 'e'
myBST[22] = 'f'
myBST[2] = 'g'
myBST[4] = 'h'
myBST[8] = 'i'
myBST[12] = 'j'
myBST[6] = 'k'
myBST[9] = 'l'
myBST[14] = 'm'
myBST[7] = 'n'

print myBST[7]
print 12 in myBST
for tree1 in myBST:
    print tree1
del myBST[5]
for tree2 in myBST:
    print tree2

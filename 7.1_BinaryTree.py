
#--------------------------------------------------------------------------
# Define a binary tree using List
def BinaryTree(root):
    return [root, [], []]

def insertLeft(root, branch):
    leftChild = root.pop(1)
    if len(leftChild) < 1:
        root.insert(1, [branch, [], []])
    else:
        root.insert(1, [branch, leftChild, []])
    return root

def insertRight(root, branch):
    rightChild = root.pop(2)
    if len(rightChild) < 1:
        root.insert(2, [branch, [], []])
    else:
        root.insert(2, [branch, [], rightChild])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

BTree = BinaryTree(7)
insertLeft(BTree, 2)
insertLeft(BTree, 3)
insertRight(BTree, 11)
insertRight(BTree, 9)
print BTree

leftChild = getLeftChild(BTree)
print "the left child of root 7 is:", leftChild
setRootVal(leftChild, 5)
print BTree

insertLeft(leftChild, 4)
print BTree
print getLeftChild(leftChild)

#--------------------------------------------------------------------------
# Define a binary tree using Nodes and References
class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newBranch):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newBranch)
        else:
            branch = BinaryTree(newBranch)
            branch.leftChild = self.leftChild
            self.leftChild = branch

    def insertRight(self, newBranch):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newBranch)
        else:
            branch = BinaryTree(newBranch)
            branch.rightChild = self.rightChild
            self.rightChild = branch

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __repr__(self):
        return "current root is: {0} \nthe left child is: {1} \nthe right child is: {2}".format(self.key, self.leftChild, self.rightChild)

    def __iter__(self):
        if self != None:
            yield self.key
            if self.leftChild != None:
                for elem in self.leftChild:
                    yield elem
            if self.rightChild != None:
                for elem in self.rightChild:
                    yield elem

BTree2 = BinaryTree("a")
BTree2.insertLeft("b")
BTree2.insertRight("c")
BTree2.getLeftChild().insertRight("d")
BTree2.getRightChild().insertLeft("e")
BTree2.getRightChild().insertRight("f")
for branch in BTree2:
    print branch 

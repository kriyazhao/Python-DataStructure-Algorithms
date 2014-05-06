
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

    def preorder(self):
        print self.getRootVal()
        if self.leftChild != None:
            self.leftChild.preorder()
        if self.rightChild != None:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild != None:
            self.leftChild.inorder()
        print self.getRootVal()
        if self.rightChild != None:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild != None:
            self.leftChild.postorder()
        if self.rightChild != None:
            self.rightChild.postorder()
        print self.getRootVal()

BTree2 = BinaryTree("a")
BTree2.insertLeft("b")
BTree2.insertRight("c")
BTree2.getLeftChild().insertRight("d")
BTree2.getRightChild().insertLeft("e")
BTree2.getRightChild().insertRight("f")
BTree2.preorder()
BTree2.inorder()
BTree2.postorder()


#---------------------------------------------------------------------------
# Define a function to traversal a tree in a preorder manner
def preorder(tree):
    if tree != None:
        print tree.getRootVal()
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

preorder(BTree2)

#---------------------------------------------------------------------------
# Define a function to traversal a tree in a inorder manner
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print tree.getRootVal()
        inorder(tree.getRightChild())
        
inorder(BTree2)

#---------------------------------------------------------------------------
# Define a function to print expression using inorder traversal
def inorderExpr(tree):
    expression = ""
    if tree != None:
        expression = "(" + inorderExpr(tree.getLeftChild())
        expression += str(tree.getRootVal())
        expression = expression + inorderExpr(tree.getRightChild()) + ")"
        lPar = expression.find('(')
        rPar = expression.find(')')
        if lPar != -1 and rPar != -1 and expression[lPar+1: rPar].isdigit():
            expression = expression[lPar+1: rPar]
    return expression

print inorderExpr(myParseTree)

#---------------------------------------------------------------------------
# Define a function to traversal a tree in a postorder manner
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print tree.getRootVal()

postorder(BTree2)

import operator
#---------------------------------------------------------------------------
# Define a function to evaluate a parse tree in a postorder manner
def postorderEval(tree):
    operators = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftChild = None
    rightChild = None
    if tree.getLeftChild() != None:
        leftChild = postorderEval(tree.getLeftChild())
    if tree.getRightChild() != None:
        rightChild = postorderEval(tree.getRightChild())
    if leftChild and rightChild:
        return operators[tree.getRootVal()](leftChild, rightChild)
    else:
        return tree.getRootVal()

print postorderEval(BTree2)

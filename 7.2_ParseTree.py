from datastructure import Stack, BinaryTree

#---------------------------------------------------------------------------
# Define a function to build a parse tree for fully parenthesized expression
# The stack structure is for storing the parent tree
def parseTreeBuilder(inputExpr):
    exprList = inputExpr.split(" ")
    parseTree = BinaryTree("")
    parentRoot = Stack()
    parentRoot.push(parseTree)
    currentRoot = parseTree
    for token in exprList:
        if token == "(":
            currentRoot.insertLeft("")
            parentRoot.push(currentRoot)
            currentRoot = currentRoot.getLeftChild()
        elif token not in ['+','-','*','/',')']:
            currentRoot.setRootVal(int(token))
            currentRoot = parentRoot.pop()
        elif token in ['+','-','*','/']:
            currentRoot.setRootVal(token)
            currentRoot.insertRight("")
            parentRoot.push(currentRoot)
            currentRoot = currentRoot.getRightChild()
        elif token == ")":
            currentRoot = parentRoot.pop()
        else:
            raise ValueError
    return parseTree

myParseTree = parseTreeBuilder("( ( 7 * 9 ) ) + 10")
print myParseTree

import operator
#---------------------------------------------------------------------------
# Define a function to evaluate a parse tree and return calculation result
def parseTreeEvaluator(parseTree):
    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()
    if leftChild and rightChild:
        oper = operators[parseTree.getRootVal()]
        return oper(parseTreeEvaluator(leftChild), parseTreeEvaluator(rightChild))
    else:
        return parseTree.getRootVal()
    
print "the calculation result is:",parseTreeEvaluator(myParseTree)

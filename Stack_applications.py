# ----------------------------------------------------------------------------------------------------------
# SampleCode_Ting.py
# Created on: 2013-04-07 10:53:10.00000
# Author: Ting Zhao
# Usage: define some functions that use Stack structure
# Description: create some functions using Stack class:
#              - revString()       reverse a string using Stack                 O(n)
#              - parChecker()      check simple balanced parentheses            O(n)
#              - symChecker()      check balanced symbols                       O(n)
#              - DecimalToBinary() convert decimal numbers to binary numbers    O(logn)
#              - DecimalToBase()   convert decimal numbers to any base numbers  O(logn) - worst scenario
#              - infixToPostfix()  transform infix to postfix expression        O(n)
#              - postfixEva()      postfix expression evaluation                O(n)
# ----------------------------------------------------------------------------------------------------------

from datastructure import Stack

#------------------------------------
# reverse a string using Stack
def revString(item):
    astack = Stack()
    revstring = ""
    for i in item:
        astack.push(i)
    for j in range(len(item)):
        revstring += astack.pop()
    return revstring

testString = "apple"
print revString(testString)

#------------------------------------
# check simple balanced parentheses
def parChecker(parString):
    s = Stack()
    for par in parString:
        if par == "(":
            s.push(par)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    return s.isEmpty()

testString1 = "()()((()))()"
testString2 = "((())"
testString3 = "(()))"
print parChecker(testString1)
print parChecker(testString2)
print parChecker(testString3)               

#------------------------------------
# check balanced symbols
def symChecker(symString):
    s = Stack()
    for sym in symString:
        if sym in "({[":
            s.push(sym)
        else:
            if s.isEmpty():
                return False
            else:
                matSym = s.pop()
                if not matchChecker(matSym,sym):
                    return False
    return s.isEmpty()

def matchChecker(sym1, sym2):
    openSym = "({["
    closeSym = ")}]"
    return openSym.index(sym1) == closeSym.index(sym2)

testString1 = "{{([][])}()}"
testString2 = "[{()]"
testString3 = "{[()]"
print symChecker(testString1)
print symChecker(testString2)
print symChecker(testString3)               

#------------------------------------
# convert decimal numbers to binary numbers
def DecimalToBinary(decNum):
    binString = ""
    binStack = Stack()
    while decNum > 0:
        binNum = decNum % 2
        binStack.push(binNum)
        decNum = decNum // 2
    while not binStack.isEmpty():
        binString += str(binStack.pop())
    return binString

testNumber1 = 42
testNumber2 = 122
testNumber3 = 77
print DecimalToBinary(testNumber1)
print DecimalToBinary(testNumber2)
print DecimalToBinary(testNumber3)

#------------------------------------
# convert decimal numbers to any base numbers
def DecimalToBase(decNum, base):
    system = "0123456789ABCDEF"
    baseString = ""
    baseStack = Stack()
    while decNum > 0:
        baseNum = decNum % base
        baseStack.push(baseNum)
        decNum = decNum // base
    while not baseStack.isEmpty():
        baseString += system[baseStack.pop()]
    return baseString

testNumber1 = 42
testNumber2 = 122
testNumber3 = 77
print DecimalToBase(testNumber1,2)
print DecimalToBase(testNumber2,8)
print DecimalToBase(testNumber3,16)

#------------------------------------
# transform infix expression to postfix expression
def infixToPostfix(infixString):
    order = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    operatorStack = Stack()
    postfixString = []
    infixList = infixString.split()
    print infixList
    for infixEle in infixList:
        if infixEle in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            print "append %s to the output string" % infixEle
            postfixString.append(infixEle)
        elif infixEle == "(":
            print "push ( to the stack"
            operatorStack.push(infixEle)
        elif infixEle == ")":
            print "pop operator until see ("
            topOper = operatorStack.pop()
            while topOper != "(":
                print "pop %s until see (" % topOper                
                postfixString.append(topOper)
                topOper = operatorStack.pop()
        else:
            while (not operatorStack.isEmpty()) and (order[operatorStack.peek()] >= order[infixEle]):
                print "pop out %s before push %s in" % (operatorStack.peek(), infixEle)
                postfixString.append(operatorStack.pop())        
            print "push %s in the stack" % infixEle
            operatorStack.push(infixEle)
    while not operatorStack.isEmpty():
        postfixString.append(operatorStack.pop())   
    return postfixString

testString1 = "A + B * C + D * E"
testString2 = "( A + B ) * ( C + D ) + E"
testString3 = "A + ( B - ( C + D ) * ( E - F ) )"
print infixToPostfix(testString1)
print infixToPostfix(testString2)
print infixToPostfix(testString3)

#------------------------------------
# postfix expression evaluation (postfix to infix)
def postfixEva(postfixString):
    operandStack = Stack()
    postfixList = postfixString.split(" ")
    print postfixList
    for postfixEle in postfixList:
        if postfixEle in "0123456789":
            print "push %s in the operand stack." % postfixEle
            operandStack.push(postfixEle)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            mathResult = mathCal(postfixEle, int(operand1), int(operand2))
            print "calculate %s %s %s and push the result %s in the operand stack" %(operand1, postfixEle, operand2, mathResult)
            operandStack.push(mathResult)
    return operandStack.pop()
        
def mathCal(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    else:
        return False        
    
testString1 = "7 1 + 3 * 9 /"
testString2 = "1 2 5 4 + 1 7 - * - +"
testString3 = "3 4 5 * + 7 5 * +"
print postfixEva(testString1)
print postfixEva(testString2)
print postfixEva(testString3)

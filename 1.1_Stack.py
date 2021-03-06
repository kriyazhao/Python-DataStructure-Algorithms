# ---------------------------------------------------------------------------
# 1.1_Stack.py
# Created on: 2013-04-06 9:33:01.00000
# Author: Ting Zhao
# Usage: define a stack class
# Description: create a stack class and define some functions:
#              - isEmpty() O(1)
#              - push()    O(1)
#              - pop()     O(1)
#              - peek()    O(n)
#              - size()    O(n)
# ---------------------------------------------------------------------------

class Stack:
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":

    s=Stack()

    print "Is the stack empty? ", s.isEmpty()
    s.push("cat")
    s.push(200)
    print "The current last item in the stack is: ", s.peek()
    s.push(True)
    print "The size of the stack is: ", s.size()
    print "Is the stack empty? ", s.isEmpty()
    print "Pop item in the stack: ", s.pop()
    print "Pop another item in the stack: ", s.pop()
    print "The size of the stack is: ", s.size()  

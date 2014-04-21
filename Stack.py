import os, sys

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
    s.push(4)
    s.push('dog')
    print "The current last item in the stack is: ", s.peek()
    s.push(True)
    print "The size of the stack is: ", s.size()
    print "Is the stack empty? ", s.isEmpty()
    s.push(8.4)
    print "Pop item in the stack: ", s.pop()
    print "Pop another item in the stack: ", s.pop()
    print "The size of the stack is: ", s.size()  

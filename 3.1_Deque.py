# ---------------------------------------------------------------------------
# 3.1_Deque.py
# Created on: 2013-04-11 10:37:07.00000
# Author: Ting Zhao
# Usage: define a Deque class
# Description: create a deque class and define some functions:
#              - isEmpty()     O(1)
#              - addRear()     O(n)
#              - addFront()    O(1)
#              - removeRear()  O(n)
#              - removeFront() O(1)
#              - size()        O(n)
# ---------------------------------------------------------------------------

class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.insert(0,item)

    def addFront(self, item):
        self.items.append(item)
    
    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":

    d = Deque()
    print "Is the queue empty? ", d.isEmpty()
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print "Current elements in the deque are: ", d.items
    print "The size of the deque is: ", d.size()
    print "Is the deque empty? ", d.isEmpty()
    print "Remove item from the front in the deque: ", d.removeFront()
    print "Remove another item from the rear in the deque: ", d.removeRear()
    print "The size of the deque is: ", d.size()

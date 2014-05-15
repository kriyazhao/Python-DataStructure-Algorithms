# ---------------------------------------------------------------------------
# 4.1_UnorderedList.py
# Created on: 2013-04-23 10:45:18.00000
# Author: Ting Zhao
# Usage: define a Node class and a UnorderedList class
# Description: create a UnorderedList class and define some functions:
#              - Node class    define a node class to store item's properties in the list
#              - UnorderedList define a unorderedlist class
#                  - isEmpty()   O(1)
#                  - size()      O(n)
#                  - index()     O(n)
#                  - add()       O(1)
#                  - append()    O(1)
#                  - insert()    O(n)
#                  - search()    O(n)
#                  - remove()    O(n)
#                  - pop(pos)    O(n)
# ---------------------------------------------------------------------------

class Node:

    def __init__(self, firstData):
        self.data = firstData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, nextNode):
        self.next = nextNode
    
class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        # if it is the first item, assign the item to self.toe as well
        if self.head == None:
            self.tail = newNode
        self.head = newNode

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False
    
    def remove(self, item):
        if self.size() == 0:
            raise KeyError
        else:
            current = self.head
            previous = None
            while current.getNext() != None and current.getData() != item:
                previous = current
                current = current.getNext()
            # if item is found at the head position
            if previous == None:
                if self.size() == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
                if current.getNext() == None:
                    self.tail = previous

    def append(self, item):
        newNode = Node(item)
        oldTail = self.tail
        oldTail.setNext(newNode)
        self.tail = newNode
        
    def index(self, item):
        count = 0
        current = self.head
        while current.getData() != item:
            count += 1
            current = current.getNext()
        return count

    def insert(self, pos, item):
        if pos >= self.size():
            raise IndexError
        elif pos == 0:
            newNode = Node(item)
            if self.head == None:
                self.tail = newNode
            else:
                newNode.setNext(self.head)
            self.head = newNode
        else:
            count = 0
            current = self.head
            # get the node that is previous to the pos node 
            while count < (pos - 1):
                count += 1
                current = current.getNext()
            newNode = Node(item)
            newNode.setNext(current.getNext())
            current.setNext(newNode)
        
    def pop(self, pos = None):
        count = 0
        current = self.head
        previous = None
        if pos >= self.size():
            raise IndexError
            return
        else:
            if current.getNext() == None:
                self.head = None
                return current.getData()
            else:
                if pos == None:
                    while current.getNext() != None:
                        previous = current
                        current = current.getNext()
                    previous.setNext(current.getNext())
                    self.tail = previous
                    return current.getData()
                else:
                    while count < pos:
                        count += 1
                        previous = current
                        current = current.getNext()
                    previous.setNext(current.getNext())
                    return current.getData()
                    
myList = UnorderedList()
myList.add(13)
myList.add(38)
myList.add(50)
myList.add(14)
myList.add(45)
myList.add(27)
print "the size of the list is: ", myList.size()
print "If number 14 is in the list? ", myList.search(14)
myList.remove(50)
print "the size of the list is: ", myList.size()
myList.append(70)
print "the index of number '14' is: ", myList.index(14)
myList.insert(4, 48)
print "Pop the item at position 2 in the list:", myList.pop(2)
print "Pop the last item in the ordered list:", myList.pop()
print "the size of the list is: ", myList.size()


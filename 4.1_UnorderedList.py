# ---------------------------------------------------------------------------
# 4.1_UnorderedList.py
# Created on: 2013-04-23 10:45:18.00000
# Author: Ting Zhao
# Usage: define a Node class and a UnorderedList class
# Description: create a UnorderedList class and define some functions:
#              - isEmpty() O(1)
#              - push()    O(1)
#              - pop()     O(1)
#              - peek()    O(n)
#              - size()    O(n)
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
        current = self.head
        previous = None
        result = False
        while not result:
            if not current.getData() == item:
                previous = current
                current = current.getNext()
            else:
                result = True
        # if item is found at the head position
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext()) 

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
        count = 0
        current = self.head
        # get the node that is previous to the pos node 
        while count < (pos - 1):
            count += 1
            current = current.getNext()
        newNode = Node(item)
        newNode.setNext(current.getNext())
        current.setNext(newNode)
        
    def pop(self):
        current = self.head
        next = current.getNext()
        while next.getNext() != None:
            current = next
            next = current.getNext()
        current.setNext(next.getNext())
        self.tail = current

    def pop(self, pos):
        count = 0
        current = self.head
        if pos == self.size():
            self.pop()
        else:
            while count < (pos - 1):
                count += 1
                current = current.getNext()
            current.setNext(current.getNext().getNext())

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
print "the index of number '45' is: ", myList.index(45)
myList.insert(4, 48)
myList.pop(2)
print "the size of the list is: ", myList.size()


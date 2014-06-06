# ---------------------------------------------------------------------------
# 4.2_OrderedList.py
# Created on: 2013-04-27 15:45:23.00000
# Author: Ting Zhao
# Usage: define a Node class and an OrderedList class
# Description: create an OrderedList class and define some functions:
#              - Node class    define a node class to store item's properties in the list
#              - OrderedList   define an orderedlist class (ascending order)
#                  - isEmpty()   O(1)
#                  - size()      O(n)
#                  - index()     O(n)
#                  - add()       O(1)
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
    
class OrderedList:

    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def index(self, item):
        count = 0
        current = self.head
        while current.getData() != item and current.getNext() != None:
            count += 1
            current = current.getNext()
        if current.getData() != item:
            raise KeyError("item cannot be found in the linked list!")
            return
        else:
            return count

    def add(self, item):
        current = self.head
        previous = None
        while item > current.getData() and current.getNext() != None:
            previous = current
            current = current.getNext()
        newNode = Node(item)
        if item < current.getData():
            newNode.setNext(current)
            if previous == None:
                self.head = newNode
            else:
                previous.setNext(newNode)
        else:
            current.setNext(newNode)

    def search(self, item):
        current = self.head
        while current != None:
            if item == current.getData():
                return True
            elif item < current.getData():
                return False
            else:
                current = current.getNext()
        return False
    
    def remove(self, item):
        if self.size() == 0:
            raise IndexError("pop from an empty linked list!")
            return
        current = self.head
        previous = None
        while current.getData() < item and current.getNext() != None:
            previous = current
            current = current.getNext()
        if current.getData() != item:
            raise KeyError("item cannot be found in the linked list!")
            return 
        else:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            
    def pop(self, pos = None):
        if self.size() == 0:
            raise IndexError("pop from an empty linked list!")
            return
        if pos > self.size() or pos < 0:
            raise IndexError("position is out of bound!")
            return
        elif pos == None:
            pos = self.size() - 1
        elif type(pos) is not int:
            raise TypeError("position is not an integer!")
            return
        else:
            count = 0
            current = self.head
            previous = None
            while count < pos:
                count += 1
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return current.getData()
            
myList = OrderedList()
myList.add(13)
myList.add(38)
myList.add(50)
myList.add(14)
myList.add(45)
myList.add(27)
print "the size of the list is:", myList.size()
print "If number 14 is in the list?", myList.search(14)
myList.remove(50)
print "Pop the last item in the ordered list:", myList.pop()
print "Pop the item at position 3 in the list:", myList.pop(3)
print "the size of the list is: ", myList.size()


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
        while current.getData() != item:
            if current.getNext != None:
                count += 1
                current = current.getNext()
            else:
                raise IndexError
        return count

    def add(self, item):
        current = self.head
        previous = None
        while current != None:
            if item < current.getData():
                break
            else:
                previous = current
                current = current.getNext()
        newNode = Node(item)
        newNode.setNext(current)
        if previous == None:
            self.head = newNode
        else:
            previous.setNext(newNode)

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
                else:
                    while count < pos:
                        count += 1
                        previous = current
                        current = current.getNext()
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


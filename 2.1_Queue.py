# ---------------------------------------------------------------------------
# 2.1_Queue.py
# Created on: 2013-04-09 11:12:37.00000
# Author: Ting Zhao
# Usage: define a Queue class
# Description: create a queue class and define some functions:
#              - isEmpty() O(1)
#              - enqueue() O(n)
#              - dequeue() O(1)
#              - size()    O(n)
# ---------------------------------------------------------------------------

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == "__main__":

    q = Queue()
    print "Is the queue empty? ", q.isEmpty()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print "Current elements in the queue are: ", q.items
    print "The size of the queue is: ", q.size()
    print "Is the queue empty? ", q.isEmpty()
    print "dequeue item in the queue: ", q.dequeue()
    print "dequeue another item in the queue: ", q.dequeue()
    print "The size of the queue is: ", q.size()

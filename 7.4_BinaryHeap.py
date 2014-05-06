
#-----------------------------------------------------------------------------
# Define a binary heap class
class BinaryHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, item): # O(logn)
        self.heapList.append(item)
        self.currentSize += 1
        parentIndex = self.currentSize // 2
        while parentIndex > 0:
            if item < self.heapList[parentIndex]:
                temp = self.heapList[parentIndex]
                self.heapList[parentIndex] = item
                self.heapList[self.currentSize] = temp
            parentIndex = parentIndex // 2

    def findMin(self):
        return self.heapList[1]

    def delMin(self): # O(logn)
        minVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        currentIndex = 1
        self.filterDown(currentIndex)
        return minVal

    def filterDown(self, currentIndex): # O(logn)
        while (2 * currentIndex) <= self.currentSize:
            print "currentIndex:", currentIndex
            leftIndex = 2 * currentIndex
            minIndex = leftIndex
            if leftIndex + 1 < self.currentSize and self.heapList[leftIndex] > self.heapList[leftIndex + 1]:
                minIndex = leftIndex + 1
            if self.heapList[currentIndex] > self.heapList[minIndex]:
                temp = self.heapList[minIndex]
                self.heapList[minIndex] = self.heapList[currentIndex]
                self.heapList[currentIndex] = temp
                currentIndex = minIndex
            else:
                break
            print self.heapList
    
    def isEmpty(self):
        return self.currentSize <= 1
    
    def size(self):
        return self.currentSize

    def buildHeap(self, inputList): # O(n)
        self.heapList = [0] + inputList
        self.currentSize = len(inputList)
        currentIndex = self.currentSize // 2 # start in the middle of the heaplist since the other half are all leaves
        while currentIndex > 0:
            self.filterDown(currentIndex)
            currentIndex -= 1

    def heapSort(self, inputList): # O(nlogn)
        self.buildHeap(inputList)
        sortedList = []
        while self.currentSize >= 1:
            sortedList.append(self.delMin())
        return sortedList

myHeapList = BinaryHeap()
myHeapList.buildHeap([13,11,5,7,15,9,10])
print myHeapList.delMin()
print myHeapList.heapSort([13,11,5,7,15,9,10])

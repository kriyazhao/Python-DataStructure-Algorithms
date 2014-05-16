import UnorderedList()

myList = UnorderedList()
myList.add(13)
myList.add(38)
myList.add(50)
myList.add(14)
myList.add(45)
myList.add(27)
print "the size of the list is: ", myList.size()
print "If number 14 is in the list? ", myList.search(14)
#myList.remove(50)
print "the size of the list is: ", myList.size()
myList.append(70)
print "the index of number '14' is: ", myList.index(14)
myList.insert(4, 48)
#print "Pop the item at position 2 in the list:", myList.pop(2)
#print "Pop the last item in the ordered list:", myList.pop()
#print "the size of the list is: ", myList.size()

print "=================================="

def getSlice(MLL, first, last):
    current = MLL.head
    while current != first:
        current = current.getNext()
    sliceLL = UnorderedList()
    while current != last.getNext():
        sliceLL.append(current.getData())
        current = current.getNext()
    return sliceLL

def getMid(MLL, first, last):
    current = MLL.head
    while current != first:
        current = current.getNext()
    faster = current
    while faster.getNext().getNext() != last.getNext():            
        current = current.getNext()
        if faster.getNext().getNext() == last:
            break
        else:
            faster = faster.getNext().getNext()
    return current

def MergeSort(MLL, first, last):
    if first != last:
        mid = getMid(MLL, first, last)      
        MergeSort(MLL, first, mid)
        MergeSort(MLL, mid.getNext(), last)

        leftLL = getSlice(MLL, first, mid)
        rightLL = getSlice(MLL, mid.getNext(), last)
        leftNode = leftLL.head
        rightNode = rightLL.head
        mergeNode = first
        
        while leftNode != None and rightNode != None:
            if leftNode.getData() < rightNode.getData():
                mergeNode.setData(leftNode.getData())
                leftNode = leftNode.getNext()
            else:
                mergeNode.setData(rightNode.getData())
                rightNode = rightNode.getNext()
            mergeNode = mergeNode.getNext()
        while leftNode != None:
            mergeNode.setData(leftNode.getData())
            leftNode = leftNode.getNext()
            mergeNode = mergeNode.getNext()
        while rightNode != None:
            mergeNode.setData(rightNode.getData())
            rightNode = rightNode.getNext()
            mergeNode = mergeNode.getNext()
    else:
        return
current = myList.head
while current != None:
    print current.getData()
    current = current.getNext()
    
MergeSort(myList, myList.head, myList.tail)

current = myList.head
while current != None:
    print current.getData()
    current = current.getNext()

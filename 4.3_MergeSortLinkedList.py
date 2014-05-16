import UnorderedList

#===========================================================================

myList = UnorderedList()
myList.add(13)
myList.add(38)
myList.add(50)
myList.add(14)
myList.add(45)
myList.add(27)
myList.append(70)
myList.insert(4, 48)

#===========================================================================

def getSlice(MLL, first, last):
    #  a function validating input params should be added later on
    current = MLL.head
    while current != first:
        current = current.getNext()
    sliceLL = UnorderedList()
    while current != last.getNext():
        sliceLL.append(current.getData())
        current = current.getNext()
    return sliceLL

def getMid(MLL, first, last):
    #  a function validating input params should be added later on
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
    #  a function validating input params should be added later on
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

#===========================================================================

MergeSort(myList, myList.head, myList.tail)

current = myList.head
while current != None:
    print current.getData()
    current = current.getNext()

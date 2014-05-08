
#----------------------------------------------------------------------------------
# Define Bubble Sort
def bubbleSort(inputList):
    for num in range(len(inputList) - 1, 0, -1):
        for index in range(num):
            if inputList[index] > inputList[index + 1]:
                temp = inputList[index]
                inputList[index] = inputList[index + 1]
                inputList[index + 1] = temp

myList = [11, 15, 5, 23, 50, 7, 45, 38, 2]
bubbleSort(myList)
print "Bubble Sort: "
print myList

#----------------------------------------------------------------------------------
# Define a revised Bubble Sort that can stop if no exchange is made during a pass
def revisedBubbleSort(inputList):
     for num in range(len(inputList) - 1, 0, -1):
        exchange = False
        for index in range(num):
            if inputList[index] > inputList[index + 1]:
                temp = inputList[index]
                inputList[index] = inputList[index + 1]
                inputList[index + 1] = temp
                exchange = True
        if exchange == False:
            return
myList = [11, 15, 5, 23, 50, 7, 45, 38, 2]
revisedBubbleSort(myList)
print "Revised Bubble Sort: "
print myList
        
#----------------------------------------------------------------------------------
# Define Selection Sort
def selectionSort(inputList):
    for num in range(len(inputList) - 1, 0, -1):
        maxPos = 0
        for index in range(num):
            if inputList[index] > inputList[maxPos]:
                maxPos = index
        temp = inputList[maxPos]
        inputList[maxPos] = inputList[num]
        inputList[num] = temp 

myList = [11, 15, 5, 23, 50, 7, 45, 38, 2]
selectionSort(myList)
print "Selection Sort: "
print myList

#----------------------------------------------------------------------------------
# Define Insertion Sort
def insertionSort(inputList):
    for index in range(len(inputList)):
        subIndex = index
        temp = inputList[index + 1]
        while temp < inputList[subIndex] and subIndex >= 1:
            inputList[subIndex + 1] = inputList[subIndex]
            subIndex -= 1
        inputList[subIndex] = temp
        
myList = [11, 15, 5, 23, 50, 7, 45, 38, 2]
selectionSort(myList)
print "Insertion Sort: "
print myList

#----------------------------------------------------------------------------------
# Define Shell Sort
def shellSort(inputList, increment):
    subListLen = len(inputList) // increment
    while subListLen > 0:
        for subListStart in range(subListLen):
            gapInsertionSort(inputList, subListStart, subListLen)
        subListLen = subListLen // increment

def gapInsertionSort(inputList, subListStart, gap):
    for index in range(subListStart, len(inputList), gap):
        subIndex = index
        temp = inputList[index]
        while subIndex >= gap and temp < inputList[subIndex - gap]:
            inputList[subIndex] = inputList[subIndex - gap]
            subIndex -= gap
        inputList[subIndex] = temp

myList = [11, 15, 5, 23, 50, 7, 45, 38, 2]
shellSort(myList, 2)
print "Shell Sort: "
print myList

#----------------------------------------------------------------------------------
# Define Merge Sort
def mergeSort(inputList, first, last):
    if len(inputList[first:last]) > 1:
        midSplit = first + len(inputList[first:last]) // 2
        mergeSort(inputList, first, midSplit)
        mergeSort(inputList, midSplit, last)

        leftIndex = 0
        rightIndex = 0
        mergeIndex = 0
        leftList = inputList[first:midSplit]
        rightList = inputList[midSplit:last]
        while leftIndex < len(leftList) and rightIndex < len(rightList):
            if leftList[leftIndex] < rightList[rightIndex]:
                inputList[first + mergeIndex] = leftList[leftIndex]
                leftIndex += 1
            else:
                inputList[first + mergeIndex] = rightList[rightIndex]
                rightIndex += 1
            mergeIndex += 1
        while leftIndex < len(leftList):
            inputList[first + mergeIndex] = leftList[leftIndex]
            leftIndex += 1
            mergeIndex += 1
        while rightIndex < len(rightList):
            inputList[first + mergeIndex] = rightList[rightIndex]
            rightIndex += 1
            mergeIndex += 1
        print "Merging", leftList, "and", rightList, "into:", inputList

myList = [11, 15, 5, 23, 50, 7, 45, 38, 2]
mergeSort(myList, 0, len(myList))
print "Merge Sort: "
print myList

#----------------------------------------------------------------------------------
# Define Quick Sort
def quickSort(inputList, firstIndex, lastIndex):
    if firstIndex < lastIndex:
        leftMark = firstIndex + 1
        rightMark = lastIndex
        pivotVal = inputList[firstIndex]
        while leftMark < rightMark:
            
            while pivotVal >= inputList[leftMark] and leftMark <= rightMark and leftMark < len(inputList)-1:
                leftMark += 1
                print leftMark
            while pivotVal <= inputList[rightMark] and leftMark <= rightMark and rightMark > 1:
                rightMark -= 1
                print rightMark

            if leftMark > rightMark:
                break
            temp = inputList[leftMark]
            inputList[leftMark] = inputList[rightMark]
            inputList[rightMark] = temp
        inputList[firstIndex] = inputList[rightMark]
        inputList[rightMark] = pivotVal
        quickSort(inputList, firstIndex, rightMark - 1)
        quickSort(inputList, rightMark + 1, lastIndex)

myList = [11, 15, 5, 23, 50, 7, 45, 38, 2]
quickSort(myList, 0, len(myList) - 1)
print "Quick Sort: "
print myList    

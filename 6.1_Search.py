
#-----------------------------------------------------------------
# Define a function to perform sequential search
# case                Best case     Worst case      Avg case
# item is present     1             n               n/2
# item is not         n             n               n
def sequentialSearch(inputList, item):
    count = 0
    while count < len(inputList):
        if inputList[count] == item:
            return True
        else:
            count += 1
    return False

myList = [2, 3, 23, 13, 9, 17, 5]
print "Sequential Search:"
print "Is 9 in the list", myList, sequentialSearch(myList, 9)
print "Is 12 in the list", myList, sequentialSearch(myList, 12)

#-----------------------------------------------------------------
# Define a function to perform ordered sequential search (ascending)
# case                Best case     Worst case      Avg case
# item is present     1             n               n/2
# item is not         1             n               n/2
def orderedSequentialSearch(inputList, item):
    count = 0
    while count < len(inputList):
        if inputList[count] == item:
            return True
        elif inputList[count] > item:
            return False
        else:
            count += 1
    return False

myList = [2, 3, 5, 9, 13, 17, 23]
print "Ordered Sequential Search:"
print "Is 9 in the list", myList, orderedSequentialSearch(myList, 9)
print "Is 12 in the list", myList, orderedSequentialSearch(myList, 12)

#-----------------------------------------------------------------
# Define a function to perform binary search (ascending)
# case                Best case     Worst case      Avg case
# item is present     1             logn            logn/2
# item is not         1             logn            logn/2
def binarySearch(inputList, item):
    first = 0
    last = len(inputList) - 1
    while first <= last:
        mid = (first + last) // 2
        if inputList[mid] == item:
            return True
        elif inputList[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False

myList = [2, 3, 5, 9, 13, 17, 23]
print "Binary Search:"
print "Is 13 in the list", myList, binarySearch(myList, 13)
print "Is 4 in the list", myList, binarySearch(myList, 4)

#-----------------------------------------------------------------
# Define a recursive function to perform binary search (ascending)
def recurBinarySearch(inputList, first, last, item):
    if len(inputList[first:last]) == 0:
        return False
    else:
        mid = first + len(inputList[first:last]) // 2
        if inputList[mid] == item:
            return True
        elif inputList[mid] > item:
            return recurBinarySearch(inputList, first, mid, item)
        else:
            return recurBinarySearch(inputList, mid + 1, last, item)

myList = [2, 3, 5, 9, 13, 17, 23]
print "Recursive Binary Search:"
print "Is 13 in the list", myList, recurBinarySearch(myList, 0, len(myList) - 1, 13)
print "Is 4 in the list", myList, recurBinarySearch(myList, 0, len(myList) - 1, 4)

#-----------------------------------------------------------------
# Define a HashTable class for dictionary data type
class HashTable():
    
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashVal = self.hashFunction(key)
        if self.slots[hashVal] == None:
            self.slots[hashVal] = key
            self.data[hashVal] = value
        elif self.slots[hashVal] == key:
            self.data[hashVal] = value
        else:
            nextHash = self.reHash(hashVal)
            while self.slots[nextHash] != None and self.slots[nextHash] != key:
                nextHash = self.reHash(nextHash)
            if self.slots[nextHash] == None:
                self.slots[nextHash] = key
                self.data[nextHash] = value
            else:
                self.data[nextHash] = value
        if float(self.__len__()) / float(self.size) > 0.8:
            self.size += 10
        
    def hashFunction(self, key):
        return key % self.size

    def reHash(self, oldHash):
        return (oldHash + 1) % self.size

    def get(self, key):
        startHash = self.hashFunction(key)
        pos = startHash
        while self.slots[pos] != None:
            if self.slots[pos] == key:
                return self.data[pos]
            else:
                pos = self.reHash(pos)
                if pos == startHash:
                    return None
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        count = 0
        size = 0
        while count < self.size:
            if self.data[count] != None:
                size += 1
            count += 1
        return size
    
    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def __del__(self, key):
        rehashVal = self.hashFunction(key)
        count = 0
        while self.slots[rehashVal] != key and count < self.size:
            rehashVal = self.reHash(rehashVal)
            count += 1
        if self.slots[rehashVal] == key:
            self.slots[rehashVal] = None
            self.data[rehashVal] = None
        else:
            print key, "is not a key in the hash table!"
        
myHash = HashTable()
print "Hash Search:"
myHash[26] = "dog"
myHash[93] = "lion"
myHash[17] = "tiger"
myHash[77] = "bird"
myHash[31] = "cow"
myHash[44] = "goat"
myHash[55] = "pig"
myHash[20] = "chicken"
print myHash[93]
print myHash[44]
print "the size of myHash is:", myHash.__len__()
print "Is 'bird' in myHash?", myHash.__contains__(77)
print myHash.slots
print myHash.data
print "delete tiger", myHash.__del__(17)
print myHash.__del__(45)
print myHash.slots
print myHash.data

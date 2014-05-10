from datastructure import Stack

#-----------------------------------------------------------------
# Tower of Hanoi
def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        popOut = fromPole.pop()
        toPole.push(popOut)
        print "Moving Disk",popOut,"from", fromPole.name, "to", toPole.name
        moveTower(height-1, withPole, toPole, fromPole)

fStack = Stack()
fStack.name = "A"
tStack = Stack()
tStack.name = "B"
wStack = Stack()
wStack.name = "C"
for i in range(5, 0, -1):
    fStack.push(i)
    
moveTower(5, fStack, tStack, wStack)            

#-----------------------------------------------------------------
# Define a class with recursive function to solve "Die hard" problem
class dieHard:
    
    def __init__(self, big, small, goal):
        self.big = big
        self.small = small
        self.init = [0,0]
        self.goal = goal

    def steps(self, stateList):
        bigState, smallState = stateList
        big2small = min(bigState, self.small - smallState)
        return [(self.big, smallState), # fill the big jug
                (bigState - big2small, smallState + big2small), # pour water from big jug to small jug
                (bigState, 0), # empty small jug
                (0, smallState)] # empty big jug
    
    def dieHardSolver(self, stateList):
        currentState = stateList[len(stateList)-1]
        availableState = self.steps(currentState)
        for newState in availableState:
            try:
                if newState[0] == self.goal:
                    raise Solved(stateList + [newState])
                elif newState in stateList:
                    continue
                else:
                    tryState = stateList + [newState]
                    self.dieHardSolver(tryState)
            except Solved as e:
                print "Die Hard problem is solved!"
                print "The steps are:", e.steps
     
class Solved(Exception):
    def __init__(self, finalState):
        self.steps = finalState

myDieHard = dieHard(7, 3, 1)
myDieHard.dieHardSolver([(0, 0)])

#-----------------------------------------------------------------
# Dynamic Programming - find minimal numbers of coins for a change
def minChange(coinList, change, coinMins, coinUsed):
    for coin in range(0, change + 1):
        coinCount = coin
        newCoin = 1
        for coinCandidate in [i for i in coinList if i <= coin]:
            if coinMins[coin - coinCandidate] + 1 < coinCount:
                coinCount = coinMins[coin - coinCandidate] + 1
                newCoin = coinCandidate
        coinMins[coin] = coinCount
        coinUsed[coin] = newCoin
    return coinMins[change]        

def changePrint(change, coinUsed):
    while change > 0:
        print coinUsed[change]
        change = change - coinUsed[change]

coinList = [1, 5, 10, 25]
change = 76
coinUsed = [i * 0 for i in range(change + 2)]
coinMins = [i * 0 for i in range(change + 2)]
print "The minimum number of coins for change", change, "is:"
print minChange(coinList, change, coinMins, coinUsed)
print "They are:"
changePrint(change, coinUsed)
print coinUsed
print coinMins

#-----------------------------------------------------------------
# Dynamic Programming - find maximum profits under weight limit
def maxProfits(itemList, wtlimit, profitMaxes, itemUsed):
    for weight in range(0, wtlimit + 1):
        profitCount = weight
        newItem = 2
        itemCandidate = [i for i in itemList if i <= weight]
        if len(itemCandidate) == 0:
            continue
        else:
            for itemWeight in itemCandidate:
                if profitMaxes[weight - itemWeight] + itemList[itemWeight]> profitCount:
                    profitCount = profitMaxes[weight - itemWeight] + itemList[itemWeight]
                    newItem = itemWeight
            profitMaxes[weight] = profitCount
            itemUsed[weight] = newItem
    return profitMaxes[wtlimit]

def profitPrint(wtlimit, itemUsed):
    while wtlimit > 0:
        print itemUsed[wtlimit]
        wtlimit = wtlimit - itemUsed[wtlimit]


itemList = {2:3, 3:4, 4:6, 5:8, 7:10}
wtlimit = 20
itemUsed = [i * 0 for i in range(wtlimit + 1)]
profitMaxes = [i * 0 for i in range(wtlimit + 1)]
print "The maximum profit can be obtained under weight limit", wtlimit, "is:"
print maxProfits(itemList, wtlimit, profitMaxes, itemUsed)
print "They are:"
profitPrint(wtlimit, itemUsed)
print itemUsed
print profitMaxes

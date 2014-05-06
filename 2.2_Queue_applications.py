
# ----------------------------------------------------------------------------------------------------------
# 2.2_Queue_applications.py
# Created on: 2013-04-10 13:41:50.00000
# Author: Ting Zhao
# Usage: define some functions that use Queue structure
# Description: create some functions using Stack class:
#              - HotPotatoes()     simulate hot potato game using Queue class          O(n)
#              - simuPrintTask()   simulate printer-task scenario using Queue class    O(n)
#                - Printer class   define a printer class to store printer properties  O(1)
#                - Task class      define a task class to store task properties        O(1)
# ----------------------------------------------------------------------------------------------------------

from datastructure import Queue

#----------------------------------------------------------------
# simulate Hot Potato the Game
def hotPotatoes(nameList, cycNum):
    nameQueue = Queue()
    for name in nameList:
        print "enqueue %s in the queue" % name
        nameQueue.enqueue(name)
    while nameQueue.size() > 1:
        for i in range(cycNum-1):
            nameDeq = nameQueue.dequeue()
            print "dequeue and enqueue %s" % nameDeq
            nameQueue.enqueue(nameDeq)
        print "dequeue %s permanently" % nameQueue.dequeue()
    return nameQueue.dequeue()

nameList = ['1','2','3','4','5','6','7','8','9']
print "The last item in the queue is: ", hotPotatoes(nameList, 6)

#----------------------------------------------------------------
# simulate Printing Tasks
class Printer:

    def __init__(self, printRate):
        self.printRate = printRate
        self.currentTask = None
        self.timeRemaining = 0

    def hasTask(self):
        if self.currentTask == None:
            return False
        else:
            return True

    def startNextTask(self, task):
        self.currentTask = task
        self.timeRemaining = task.getPages() * 60 / self.printRate
        
    def countDownTime(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None    

class Task:

    def __init__(self, time):
        self.pages = random.randrange(1,21)
        self.startTime = time

    def getPages(self):
        return self.pages

    def getTimeStamp(self):
        return self.startTime

    def getWaitingTime(self, currentTime):
        return currentTime - self.startTime

def simuPrintTask(duration, printRate):
    printer = Printer(printRate)
    printQueue = Queue()
    waitingTimes = []
    for curSecond in range(duration):
        if random.randrange(1,181) == 180:
            print "There is a new task at %sth second" % curSecond
            newTask = Task(curSecond)
            print "This task has print pages of %d" % newTask.getPages()
            printQueue.enqueue(newTask)
        if (not printer.hasTask()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            print "Printer starts the next task"
            printer.startNextTask(nextTask)
            waitingTimes.append(nextTask.getWaitingTime(curSecond))
            print "Current waiting time list: ", waitingTimes
        printer.countDownTime()
        
    avgWaitingTime = sum(waitingTimes) / len(waitingTimes)
    print "Average waiting time: %d seconds" % avgWaitingTime
    print "%d tasks remaining at the moment" % printQueue.size()

for i in range(5):
    simulation(3600,8)
    

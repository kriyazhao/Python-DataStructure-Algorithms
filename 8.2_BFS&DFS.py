import Graph

#=========================================================================================
# Breadth first search class that inherit Graph class

class BFSGraph(Graph):

    def __init__(self):
        Graph.__init__(self)

    def BFS(self, startVert):
        vertQueue = Queue()
        vertQueue.enqueue(startVert)
        while vertQueue.size() > 0:
            currentVert = vertQueue.dequeue()
            print "currentVert is:", currentVert.getID()
            for nbr in currentVert.getConnections():
                print "current nbr is:", nbr.getID()
                if nbr.getColor() == "white":
                    nbr.setColor("gray")
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    print "enqueue:", nbr.getID()
                    vertQueue.enqueue(nbr)
                    currentVert.setColor("black")
                            
    def Traverse(self,targetVert):
        currentVert = targetVert
        while (currentVert.getPred()):
            print(currentVert.getID())
            currentVert = currentVert.getPred()
            print(currentVert.getID())

myBFS = BFSGraph()
for i in range(6):
    myBFS.addVertex(i)
myBFS.addEdge(0,1,5)
myBFS.addEdge(0,5,2)
myBFS.addEdge(1,2,4)
myBFS.addEdge(2,3,9)
myBFS.addEdge(3,4,7)
myBFS.addEdge(3,5,3)
myBFS.addEdge(4,0,1)
myBFS.addEdge(5,4,8)
myBFS.addEdge(5,2,1)
myBFS.BFS(myBFS.getVertex(0))
myBFS.Traverse(myBFS.getVertex(3))

#=========================================================================================
# Depth first search class that inherit Graph class

class DFSGraph(Graph):
	
    def __init__(self):
        Graph.__init__(self)
        self.time = 0
		
    def DFS(self):
        for currentVert in self:
            if currentVert.getColor() == "white":
                print "start with the current vertex:", currentVert.getID()
                self.DFSVisit(currentVert)
	
    def DFSVisit(self, startVert):
        startVert.setColor("gray")
        self.time += 1
        print "Set discovery time for vertex:", startVert.getID()
        startVert.setDiscovery(self.time)
        for nextVert in startVert.getConnections():
            if nextVert.getColor() == "white":
                nextVert.setPred(startVert)
                self.DFSVisit(nextVert)
        startVert.setColor("black")
        self.time += 1
        print "Set finish time for vertex:", startVert.getID()
        startVert.setFinish(self.time)

myDFS = DFSGraph()
for i in range(6):
    myDFS.addVertex(i)
myDFS.addEdge(0,1,5)
myDFS.addEdge(0,5,2)
myDFS.addEdge(1,2,4)
myDFS.addEdge(2,3,9)
myDFS.addEdge(3,4,7)
myDFS.addEdge(3,5,3)
myDFS.addEdge(4,0,1)
myDFS.addEdge(5,4,8)
myDFS.addEdge(5,2,1)
myDFS.DFS()
#myDFS.DFSVisit(myDFS.getVertex(0))

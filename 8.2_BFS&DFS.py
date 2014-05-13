import Graph

#=========================================================================================
# Breadth first search class that inherit Graph class

class BFSGraph(Graph):

	def __init__(self):
		super().__init__()

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

myBFS = myGragh
myBFS.BFS(myBFS.getVertex(0))
myBFS.Traverse(myBFS.getVertex(3))

#=========================================================================================
# Depth first search class that inherit Graph class

class DFSGraph(Graph):
	
	def __init__(self):
		super().__init__(self)
		self.time = 0
		
	def DFS(self):
		for currentVert in self:
			if currentVert.getColor() == "white":
				self.DFSVisit(currentVert)
	
	def DFSVisit(self, startVert):
		startVert.setColor("gray")
		self.time += 1
		startVert.setDiscovery(self.time)
		for nextVert in startVert.getConnections():
			if nextVert.getColor() == "white":
				nextVert.setPred(startVert)
				self.DFSVisit(nextVert)
		startVert.setColor("black")
		self.time += 1
		startVert.setFinish(self.time)

myDFS = myGragh
myDFS.DFSVisit(myDFS.getVertex(0))

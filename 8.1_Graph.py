#------------------------------------------------------------------------------------------------------------
# Vertex class to store node in the graph 

class Vertex:
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # store connected vertex and weight of the edge
        self.distance = 0
        self.pred = None
        self.color = "white"
        self.disTime = 0
        self.finTime = 0

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + " is connected to: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getDistance(self):
        return self.distance

    def setDistance(self, dis):
        self.distance = dis

    def getPred(self):
        return self.pred

    def setPred(self, predVert):
        self.pred = predVert

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getDiscovery(self):
        return self.disTime

    def setDiscovery(self, time):
        self.disTime = time

    def getFinish(self):
        return self.finTime

    def setFinish(self, time):
        self.finTime = time

#------------------------------------------------------------------------------------------------------------
# Graph class

class Graph:

    def __init__(self):
        self.vertList = {}
        self.vertCount = 0

    def addVertex(self, key):
        if key in self.vertList:
            raise KeyError
        else:
            self.vertCount += 1
            newVertex = Vertex(key)
            self.vertList[key] = newVertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, fromVert, toVert, cost = 0):
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

myGragh = Graph()
for i in range(6):
    myGragh.addVertex(i)
for vertID in myGragh:
    print vertID.id
myGragh.addEdge(0,1,5)
myGragh.addEdge(0,5,2)
myGragh.addEdge(1,2,4)
myGragh.addEdge(2,3,9)
myGragh.addEdge(3,4,7)
myGragh.addEdge(3,5,3)
myGragh.addEdge(4,0,1)
myGragh.addEdge(5,4,8)
myGragh.addEdge(5,2,1)
for vert in myGragh:
    for connection in vert.getConnections():
        print "{0} is connected to {1} with a cost of {2}".format(vert.getID(), connection.getID(),vert.getWeight(connection))

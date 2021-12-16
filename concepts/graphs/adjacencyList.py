#!/usr/bin/env python3.8

class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

	def getConnections(self):
		return self.connectedTo.keys()

	def __str__(self):
		return str(self.id) + " connected to " + str([x.id for x in self.connectedTo])

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			self.vertList[f] = Vertex(f)
		if t not in self.vertList:
			self.vertList[t] = Vertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	def __contains__(self, key):
		return key in self.vertList


def main():
	G = Graph()
	for i in range(6):
		G.addVertex(i)
	G.addEdge(0, 1, 2)

	for v in G:
		print(v)
		print(v.getConnections())

if __name__ == "__main__":
	main()
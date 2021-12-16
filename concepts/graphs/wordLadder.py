#!/usr/bin/env python3.8

import collections as C
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
import sys

# help(ds)
class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectionTo = {}
		self.color = "white"
		self.dist = sys.maxsize
		self.pred = None

	def addNeighbor(self, nbr, weight=0):
		self.connectionTo[nbr] = weight

	def setColor(self, color):
		self.color = color

	def setDistance(self, dist):
		self.dist = dist

	def setPred(self, pred):
		self.pred = pred

	def getColor(self):
		return self.color

	def getDistance(self):
		return self.dist

	def getPred(self):
		return self.pred

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectionTo[nbr]

	def getConnections(self):
		# return {key.id:weight for key,weight in zip(self.connectionTo.keys(), self.connectionTo.values())}
		return self.connectionTo.keys()

	def __str__(self):
		return str(self.id) + " connected to " + str([x.id for x in self.connectionTo])

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

	def getVertex(self, key):
		return self.vertList[key]

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	def __contains__(self, key):
		return key in self.vertList

def buildGraph():
	wfile = "word.txt"
	d = {}
	g = Graph()

	with open(wfile, "r") as wordfile:
		for line in wordfile.readlines():
			word = line[:-1]
			print(word)
			for i in range(len(word)):
				w = word[:i]+"_"+word[i+1:]
				if w in d:
					d[w].append(word)
				else:
					d[w] = [word]

	print(d)
	for bucket in d:
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)

	for v in g:
		print(v)
	return g

def bfs(graph, start):
	start.setDistance(0)
	start.setPred(None)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while vertQueue.size() > 0:
		currentVert = vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if nbr.getColor() == "white":
				nbr.setColor("grey")
				nbr.setDistance(currentVert.getDistance()+1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)
		currentVert.setColor("black")

def traverse(y):
	x = y
	while x.getPred():
		print(x.getId())
		x = x.getPred()
	print(x.getId())


def main():
	G = buildGraph()
	bfs(G, G.getVertex('fool'))
	traverse(G.getVertex('sage'))



if __name__ == "__main__":
	main()
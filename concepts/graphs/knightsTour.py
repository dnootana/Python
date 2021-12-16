#!/usr/bin/env python3.8

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def knightGraph(bdSize):
	global ktGraph
	ktGraph = Graph()
	for row in range(bdSize):
		for column in range(bdSize):
			nodeId = posToNodeId(row, column, bdSize)
			all_moves = genLegalMoves(row, column, bdSize)
			for e in all_moves:
				nid = posToNodeId(e[0], e[1], bdSize)
				ktGraph.addEdge(nodeId, nid)

def posToNodeId(row, column, size):
	return row * size + column

def genLegalMoves(x, y, size):
	newMoves = []
	moveOffsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)]
	for move in moveOffsets:
		new_x = x + move[0]
		new_y = y + move[1]
		if legalCoord(new_x, new_y, size):
			newMoves.append((new_x, new_y))
	return newMoves

def legalCoord(x, y, size):
	if x >= 0 and x < size and y >= 0 and y < size:
		return True
	else:
		return False

def knightTour(n, path, u, limit):
	"""
		n     : the current depth in the search tree
		path  : a list of vertices visited up to this point
		u     : the vertex in the graph we wish to explore
		limit : the number of nodes in the path
	"""
	u.setColor("Grey")
	path.append(u)
	if n < limit:
		# nbrList = list(u.getConnections())
		nbrList = orderByAvail(u)
		i = 0
		done = False
		while i < len(nbrList) and not done:
			if nbrList[i].getColor()!="Grey":
				done = knightTour(n+1, path, nbrList[i], limit)
			i += 1
		if not done:
			path.pop()
			u.setColor("White")
	else:
		done = True
	return done

def orderByAvail(n):
	resList = []
	for v in n.getConnections():
		if v.getColor() == 'white':
			c = 0
			for w in v.getConnections():
				if w.getColor() == 'white':
					c = c + 1
			resList.append((c,v))
	resList.sort(key=lambda x: x[0])
	return [y[1] for y in resList]

ktGraph = None
def main():
	global ktGraph
	n = 5
	knightGraph(n)
	path = []
	knightTour(0,path,ktGraph.getVertex(0),24)
	# A = orderByAvail(ktGraph.getVertex(0))
	print([i.id for i in path])
	print(len(path))

if __name__ == "__main__":
	main()
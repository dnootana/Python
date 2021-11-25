#!/usr/bin/env python3.8

class BinaryTree(object):
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		t = BinaryTree(newNode)
		if self.leftChild is not None:
			t.leftChild = self.leftChild
		self.leftChild = t

	def insertRight(self, newNode):
		t = BinaryTree(newNode)
		if self.rightChild is not None:
			t.rightChild = self.rightChild
		self.rightChild = t

	def getLeftVal(self):
		return self.leftChild

	def getRightVal(self):
		return self.rightChild

	def getRootVal(self):
		return self.key

	def setRootVal(self, rootObj):
		self.key = rootObj

def main():
	r = BinaryTree('a')
	print(r.getRootVal())
	r.insertLeft(2)
	print(r.getLeftVal().getRootVal())
	r.insertRight(4)
	print(r.getRightVal().getRootVal())

	
	

if __name__ == "__main__":
	main()
#!/usr/bin/env python3.8
"""Implementation of binary tree using List data structure"""

def BinaryTree(r):
	return [r,[],[]]

def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t)>1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])

def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t)>1:
		root.insert(2,[newBranch,t,[]])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root, newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

def main():
	r = BinaryTree(3)
	insertLeft(r, 4)
	insertLeft(r, 1)
	insertLeft(r, 2)
	insertRight(r[1], 9)
	insertRight(r[1][1], 8)
	insertRight(r[1][1][1], 7)
	insertRight(r[1][2], 6)
	print(r)

if __name__ == "__main__":
	main()
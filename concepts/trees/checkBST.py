#!/usr/bin/env python3.8

import BinarySearchTree as BST
import BinaryTree as BT
import MinHeap as minHeap
import MaxHeap as maxHeap

tree_vals = []
def inOrderAppend(tree):
	if tree:
		inOrderAppend(tree.getLeftVal())
		tree_vals.append(tree.getRootVal())
		inOrderAppend(tree.getRightVal())

def sort_check(tree_vals):
	return sorted(tree_vals) == tree_vals

def BSTcheck(tree):
	inOrderAppend(tree)
	print(sort_check(tree_vals))

def treeMin(node):
	if not node:
		return float("inf")
	minleft = treeMin(node.leftChild)
	minright = treeMin(node.rightChild)
	return min(minleft, node.key, minright)

def treeMax(node):
	if not node:
		return float("-inf")
	maxleft = treeMax(node.leftChild)
	maxright = treeMax(node.rightChild)
	return max(maxleft, node.key, maxright)

def verify(node):
	if not node:
		return True
	if treeMin(node.leftChild) <= node.key <= treeMax(node.rightChild):
		verify(node.leftChild) and verify(node.rightChild)
		return True
	else:
		return False

def main():
	print("For real BST : ")
	mytree = BST.BinarySearchTree()
	mytree[3]="red"
	mytree[4]="blue"
	mytree[6]="yellow"
	mytree[2]="at"
	mytree[1]="apple"
	mytree[5]="rat"
	BSTcheck(mytree.root)
	print(verify(mytree.root))
	tree_vals = []
	print("Normal Binary Tree : ")
	r = BT.BinaryTree(1)
	r.insertLeft(2)
	r.insertRight(6)
	r.insertRight(4)
	r.insertLeft(3)
	BSTcheck(r)
	print(verify(r))
	# tree_vals = []
	# print("Min Heap : ")
	# list_given = [6, 10, 34, 23, 12, 3, 5, 2, 9, 5, 3, 2, 9, 10]
	# Heap = minHeap.MinHeap()
	# Heap.buildHeap(list_given)
	# BSTcheck(Heap.heapList[1])
	# print(verify(Heap.heapList[1]))

if __name__ == "__main__":
	main()
#!/usr/bin/env python3.8

import collections

import BinaryTree as BT
import BinarySearchTree as BST
import MinHeap as minHeap
import MaxHeap as maxHeap

def levelOrderPrint(tree):
	if not tree:
		return
	currentcount = 1
	nextcount = 0
	nodelist = [tree]
	while len(nodelist) > 0:
		currentnode = nodelist.pop(0)
		print(currentnode.key,end=" ")
		currentcount -= 1

		if currentnode.leftChild:
			nodelist.append(currentnode.leftChild)
			nextcount +=1
		if currentnode.rightChild:
			nodelist.append(currentnode.rightChild)
			nextcount += 1
		if currentcount == 0:
			print("\n")
			nextcount, currentcount = currentcount, nextcount

def main():
	print("For real BST : ")
	mytree = BST.BinarySearchTree()
	mytree[11]="red"
	mytree[4]="blue"
	mytree[6]="yellow"
	mytree[2]="at"
	mytree[1]="apple"
	mytree[5]="rat"
	mytree[7]="fas"
	mytree[10]="skdf"
	mytree[19]="frqw"
	mytree[8]="afjfhj"
	levelOrderPrint(mytree.root)

	print("Normal Binary Tree : ")
	r = BT.BinaryTree(1)
	r.insertLeft(2)
	r.insertRight(6)
	r.insertRight(4)
	r.insertLeft(3)
	r.insertLeft(20)
	r.insertRight(60)
	r.insertRight(14)
	r.insertLeft(31)
	levelOrderPrint(r)

if __name__ == "__main__":
	main()
#!/usr/bin/env python3.8

import BinarySearchTree as BST

mytree = None

def trimBST(tree, minVal, maxVal):
	global mytree
	if not tree:
		return
	
	if minVal <= tree.key <= maxVal:
		tree.leftChild = trimBST(tree.leftChild, minVal, maxVal)
		tree.rightChild = trimBST(tree.rightChild, minVal, maxVal)
		return tree
	if tree.key < minVal:
		if tree == mytree.root:
			mytree.root = mytree.root.rightChild
		tree.rightChild = trimBST(tree.rightChild, minVal, maxVal)
		return tree.rightChild
	if tree.key > maxVal:
		if tree == mytree.root:
			mytree.root = mytree.root.leftChild
		tree.leftChild = trimBST(tree.leftChild, minVal, maxVal)
		return tree.leftChild

def main():
	global mytree
	print("For real BST : ")
	mytree = BST.BinarySearchTree()
	mytree[12]="red"
	mytree[4]="blue"
	mytree[6]="yellow"
	mytree[2]="at"
	mytree[1]="apple"
	mytree[5]="rat"
	mytree[7]="fas"
	mytree[10]="skdf"
	mytree[19]="frqw"
	mytree[8]="afjfhj"
	mytree[16]="skdf"
	mytree[22]="frqw"
	BST.traverse.inOrder(mytree.root)
	print("Trim BST 4, 10 : ")
	trimBST(mytree.root, 4, 16)
	BST.traverse.inOrder(mytree.root)

if __name__ == "__main__":
	main()
#!/usr/bin/env python3.8

from BinaryTree import BinaryTree


def preOrder(tree):
	"""
		<root><left><right>
	"""
	if tree:
		print(tree.getRootVal())
		preOrder(tree.getLeftVal())
		preOrder(tree.getRightVal())


def inOrder(tree):
	"""
		<left><root><right>
	"""
	if tree:
		inOrder(tree.getLeftVal())
		print(tree.getRootVal())
		inOrder(tree.getRightVal())

def postOrder(tree):
	"""
		<left><right><root>
	"""
	# list_a.append(tree.getRootVal())
	if tree:
		postOrder(tree.getLeftVal())
		postOrder(tree.getRightVal())
		print(tree.getRootVal())

r = BinaryTree('Book')
# print(r.getRootVal())

r.insertLeft("Chapter1")
# print(r.getLeftVal().getRootVal())

r.getLeftVal().insertLeft("Section 1.1")

r.getLeftVal().insertRight("Section 1.2")

r.getLeftVal().getRightVal().insertLeft("Section 1.2.1")

r.getLeftVal().getRightVal().insertRight("Section 1.2.2")

r.insertRight("Chapter2")
# print(r.getRightVal().getRootVal())

r.getRightVal().insertLeft("Section 2.1")

r.getRightVal().getLeftVal().insertLeft("Section 2.1.1")

r.getRightVal().getLeftVal().insertRight("Section 2.1.2")

r.getRightVal().insertRight("Section 2.2")

# print("Preorder Traversal")
# preOrder(r)
# print("Inorder Traversal")
# inOrder(r)
list_a = []
print("Postorder Traversal")
postOrder(r)
print(list_a)
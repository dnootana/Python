
class TreeNode(object):
	def __init__(self, key, val, left=None, right=None, parent=None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent.leftChild == self

	def isRightChild(self):
		return self.parent.rightChild == self

	def isRoot(self):
		return self.parent == None

	def isLeaf(self):
		return not (self.leftChild or self.rightChild)

	def hasAnyChildren(self):
		return self.leftChild != None or self.rightChild != None

	def hasBothChildren(self):
		return self.leftChild != None and self.rightChild != None

	def ReplaceNodeData(self, key, val, left, right):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		if self.leftChild:
			self.leftChild.parent = self
		if self.rightChild:
			self.rightChild.parent = self

class BinarySearchTree(object):
	def __init__(self, ):
		self.root = None
		self.size = 0

	def __len__(self):
		return self.size

	def length(self):
		return self.size

	def put(self, key, val):
		if self.root:
			self._put(key, val, self.root)
		else:
			self.root = TreeNode(key, val)
			self.size += 1

	def _put(self, key, val, currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key, val, currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key, val, parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key, val, currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key, val, parent=currentNode)

	def __setitem__(self, key, val):
		self.put(key, val)

	def get(self, key):
		if self.root:
			res = self._get(key, self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def _get(self, key, currentNode):
		if not currentNode:
			return None
		elif key == currentNode.key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key, currentNode.leftChild)
		else:
			return self._get(key, currentNode.rightChild)

	def __getitem__(self, key):
		return self.get(key)

	def __contains__(self, key):
		if self._get(key, self.root):
			return True
		else:
			return False

	def delete(self, key):
		if self.size > 1:
			nodeToRemove = self._get(key, self.root)
			if nodeToRemove == None:
				raise keyError("Error, key not found!")
			else:
				self.remove(nodeToRemove)
				self.size -= 1
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = 0
		else:
			raise keyError("Error, key not found!")

	def __delItem__(self, key):
		self.delete(key)

	def findSuccessor(self):
		
		succ = None
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		else:
			pass

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		else:
			if self.isLeftChild():
				self.parent.leftChild = self.rightChild
				self.rightChild.parent = self.parent
			else:
				self.parent.rightChild = self.rightChild
				self.rightChild.parent = self.parent

	def findMin(self):
		current = self
		while current.hasLeftChild():
			current = current.leftChild
		return current

	def remove(self, currentNode):
		if currentNode.isLeaf():
			if currentNode.parent.leftChild == currentNode:
				currentNode.parent.leftChild = None
			else:
				currentNode.parent.rightChild = None
		elif currentNode.hasBothChildren():
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key = succ.key
			currentNode.payload = succ.payload
		else:
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
					currentNode.parent.leftChild = currentNode.leftChild
					currentNode.leftChild.parent = currentNode.parent
				elif currentNode.isRightChild():
					currentNode.parent.rightChild = currentNode.leftChild
					currentNode.leftChild.parent = currentNode.parent
				else:
					self.ReplaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload, currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
			else:
				if currentNode.isLeftChild():
					currentNode.parent.leftChild = currentNode.rightChild
					currentNode.leftChild.parent = currentNode.parent
				elif currentNode.isRightChild():
					currentNode.parent.rightChild = currentNode.rightChild
					currentNode.rightChild.parent = currentNode.parent
				else:
					self.ReplaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload, currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)


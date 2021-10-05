#!/usr/bin/env python3.8

class Node(object):
	def __init__(self, value):
		self.value = value
		self.nextnode = None
		self.prevnode = None

	def get_data(self):
		return self.value

	def set_nextnode(self, nextnode):
		self.nextnode = nextnode

	def set_prevnode(self, prevnode):
		self.prevnode = prevnode

	def get_nextnode(self):
		return self.nextnode

	def get_prevnode(self):
		return self.prevnode

class DoublyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_head(self, item):
		new_node = Node(item)
		new_node.set_prevnode(None)
		new_node.set_nextnode(self.head)
		if not self.tail:
			self.tail = new_node
		self.head = new_node

	def insert_tail(self, item):
		new_node = Node(item)
		new_node.set_prevnode(self.tail)
		if self.tail:
			self.tail.set_nextnode(new_node)
		if not self.head:
			self.head = new_node
		self.tail = new_node

	def insert_between(self, item, prev_data):
		new_node = Node(item)
		current = self.head
		while current:
			if current.get_data() == prev_data:
				new_node.set_nextnode(current.get_nextnode())
				new_node.set_prevnode(current)
				current.set_nextnode(new_node)
				current.get_nextnode().set_prevnode(new_node)
				return True
			current = current.get_nextnode()
		return False

	def delete_head(self):
		self.head = self.head.get_nextnode()
		if self.head:
			self.head.set_prevnode(None)

	def delete_tail(self):
		self.tail = self.tail.get_prevnode()
		if self.tail:
			self.tail.set_nextnode(None)

	def delete_item(self, item):
		current = self.head
		previous = None
		while current:
			if current.get_data() == item:
				if previous:	
					previous.set_nextnode(self.current.get_nextnode())
			previous = current
			current = self.current.get_nextnode()
		return ValueError("Not Found")

	def search_item(self, item):
		current = self.head
		while current:
			if current.get_data() == item:
				return current
			current = self.current.get_nextnode()
		return ValueError("Not Found")

	def size(self):
		count = 0
		current = self.head
		while current:
			current = current.get_nextnode()
			count += 1
		return count

	def traverse(self):
		data = []
		current = self.head
		while current:
			data.append(current.get_data())
			current = current.get_nextnode()
		return data


a = DoublyLinkedList()
a.insert_head(1)
a.insert_tail(2)
a.insert_head(0)
a.insert_tail(3)
a.insert_tail(4)
print(a.head.get_data())
print(a.tail.get_data())
print(a.size())
print(a.traverse())
a.delete_head()
print(a.size())
print(a.traverse())
a.delete_tail()
print(a.traverse())
a.delete_tail()
print(a.traverse())
a.delete_tail()
print(a.traverse())
a.delete_tail()
print(a.traverse())
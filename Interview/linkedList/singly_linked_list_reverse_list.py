#!/usr/bin/env python3.8

"""
Given a singly linked list, write a function which reverses the given linked list
0->1->2->3->4->5->6->7->8
should return 0<-1<-2<-3<-4<-5<-6<-7<-8
"""

import sys
sys.path.append('../')
import singly_linked_list as SLinked_List
from stackQueueDeque.stack import Stack

class Reverse_list(SLinked_List.SinglyLinkedList):

	# Iterative Method
	def reserse_list(self):
		prev = None
		curr = self.head
		nexT = None
		while curr:
			nexT = curr.nextnode
			curr.set_nextnode(prev)

			prev = curr
			curr = nexT
		self.head, self.tail = self.tail, self.head

	# Recursive Method
	def reserse_list1(self, head=None):
		if head is None:
			head = self.head
			self.tail = head

		if head.nextnode is None:
			self.head = head
			return

		self.reserse_list1(head.nextnode)
		head.nextnode.nextnode = head
		head.nextnode = None
		return

	# Using Stack
	def reserse_list2(self):
		temp = self.head
		stack = Stack()
		while temp:
			stack.push(temp)
			temp = temp.nextnode
		self.head = temp = stack.pop()
		while stack.size!=0:
			temp.nextnode = stack.pop()
			temp = temp.nextnode
		temp.nextnode = None
		return

l = Reverse_list()
l.insert_tail(0)
l.insert_tail(1)
l.insert_tail(2)
l.insert_tail(3)
l.insert_tail(4)
l.insert_tail(5)
l.insert_tail(6)
l.insert_tail(7)
l.insert_tail(8)
# l.reserse_list()
# l.reserse_list1()
l.reserse_list2()
print(l.traverse())
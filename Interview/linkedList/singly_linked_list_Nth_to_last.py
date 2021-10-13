#!/usr/bin/env python3.8

"""
Write a function that takes an integer value N and then returns the nth to last node in the linked list
0->1->2->3->4->5->6->7->8
should return 5 for N=4
"""
import singly_linked_list as SLinked_List

class Nth_to_Last(SLinked_List.SinglyLinkedList):
	#using runner
	def get_nth_to_last(self, N):
		back = front = self.head
		for i in range(N):
			front = front.nextnode
		while front:
			back = back.nextnode
			front = front.nextnode
		return back.value

	#recursive
	def get_nth_to_last1(self, N):
		i = 0
		node_value = None
		def get_node(self, N, temp=None):
			nonlocal i, node_value
			if temp is None:
				return
			get_node(self, N, temp.nextnode)
			i += 1
			if i == N:
				node_value = temp
			return node_value.value
		return get_node(self, N, self.head)

	#using length
	def get_nth_to_last2(self, N):
		size = self.size()
		temp = self.head
		for i in range(size-N):
			temp = temp.nextnode
		return temp.value


l = Nth_to_Last()
l.insert_tail(0)
l.insert_tail(1)
l.insert_tail(2)
l.insert_tail(3)
l.insert_tail(4)
l.insert_tail(5)
l.insert_tail(6)
l.insert_tail(7)
l.insert_tail(8)
print(l.traverse())
print(l.get_nth_to_last(1))
print(l.get_nth_to_last1(1))
print(l.get_nth_to_last2(1))
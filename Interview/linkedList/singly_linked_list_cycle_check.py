#!/usr/bin/env python3.8

import singly_linked_list as SLinked_List

#using OOP
class lList_checks(SLinked_List.SinglyLinkedList):
	#hashmap
	def cycle_check(self):
		s = set()
		temp = self.head
		while temp:
			if temp in s:
				print(temp.value, end=" -> ")
				return True
			s.add(temp)
			temp = temp.nextnode
		return False

	#Runner Technique
	def cycle_check1(self):
		temp = self.head
		runner = self.head
		while runner:
			temp = temp.nextnode
			runner = runner.nextnode.nextnode
			if temp == runner:
				temp = self.head
				while temp != runner:
					temp = temp.nextnode
					runner = runner.nextnode
					print(temp.value)
				print(temp.value, end=" -> ")
				return True
		return False

l = lList_checks()
l.insert_tail(0)
l.insert_tail(1)
l.insert_tail(2)
l.insert_tail(3)
l.insert_tail(4)
l.insert_tail(5)
l.insert_tail(6)
l.insert_tail(7)
l.insert_tail(8)


print(l.head.value)
print(l.traverse())
print("linked list is", "a cycle" if l.cycle_check() else "not a cycle")

#creating loop
l.tail.set_nextnode(l.head)

print("linked list is", "a cycle" if l.cycle_check() else "not a cycle")
print("linked list is", "a cycle" if l.cycle_check1() else "not a cycle")

#without using OOP
#hashmap
def cycle_check(lList):
	s = set()
	temp = lList.head
	while temp:
		if temp in s:
			return True
		s.add(temp)
		temp = temp.nextnode
	return False

#Runner Technique
def cycle_check1(lList):
	temp = lList.head
	runner = lList.head.nextnode
	while runner:
		if temp == runner:
			return True
		temp = temp.nextnode
		runner = runner.nextnode.nextnode
	return False

l = SLinked_List.SinglyLinkedList()
l.insert_tail(0)
l.insert_tail(1)
l.insert_tail(2)
l.insert_tail(3)
l.insert_tail(4)
l.insert_tail(5)
l.insert_tail(6)
l.insert_tail(7)
l.insert_tail(8)

print("linked list is", "a cycle" if cycle_check(l) else "not a cycle")

#creating loop
l.tail.set_nextnode(l.head.nextnode.nextnode)

print("linked list is", "a cycle" if cycle_check(l) else "not a cycle")
print("linked list is", "a cycle" if cycle_check1(l) else "not a cycle")
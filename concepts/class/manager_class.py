#!/usr/bin/env python3.8

from employee_class import Employee
from developer_class import Developer

class Manager(Employee):
	def __init__(self, fname, lname, pay, employees=None):
		super().__init__(fname, lname, pay)
		# Employee.__init__(self, fname, lname, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print("--->",emp.fullname1())

def main():
	emp1 = Employee("S", "P", 1000)
	emp2 = Employee("E", "Q", 2000)
	mang3 = Manager("R", "L", 3000)
	mang4 = Manager("T", "W", 4000, [emp1, emp2])
	print(mang4.__dict__)

	mang3.add_employee(mang4)

	mang3.print_emps()
	mang4.print_emps()

	print("isinstance")
	print(isinstance(mang4, Employee))
	print(isinstance(mang4, Developer))
	print(isinstance(mang4, Manager))
	print("issubclass")
	print(issubclass(Developer, Employee))
	print(issubclass(Manager, Employee))
	print(issubclass(Developer, Manager))

if __name__ == "__main__":
	main()

#!/usr/bin/env python3.8

class Employee:
	raise_amount = 1.04    #class variable
	no_of_employees = 0
	def __init__(self, fname, lname, salary):   #dunder method
		self.fname = fname               #instance variable
		self.lname = lname
		self.salary = int(salary)
		#self.email = fname + "." + lname + "@company.com"
		Employee.no_of_employees += 1   #class variable

	def fullname1(self):                  #regular method
		return "{} {}".format(self.fname, self.lname)

	def apply_raise(self):
		# self.salary = self.salary * Employee.raise_amount # directly checks class variable
		self.salary = self.salary * self.raise_amount #checks if instance variable exists else gets class variable

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_string):
		fname, lname, salary = emp_string.split("-")
		return cls(fname, lname, salary)

	@staticmethod
	def is_workday(day):
		if day.weekday == 5 or day.weekday == 6:
			return False
		else:
			return True

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.salary)

	def __str__(self):
		return "{} - {}".format(self.fullname1(), self.email)

	def __add__(self, other):
		return self.salary + other.salary

	def __len__(self):
		return len(self.fullname1())

	@property	
	def email(self):
		return "{}.{}@company.com".format(self.fname, self.lname)

	@property
	def fullname(self):                  #regular method
		return "{} {}".format(self.fname, self.lname)

	@fullname.setter
	def fullname(self, fullname):
		fname, lname = fullname.split(" ")
		self.fname = fname
		self.lname = lname

	@fullname.deleter
	def fullname(self):
		self.fname = None
		self.lname = None

def main():
	emp1 = Employee("Nootana", "D", 1000)

	print(emp1)
	print(emp1.fullname1())
	print(emp1.__dict__)
	emp1.apply_raise()
	print(emp1.salary)

	Employee.set_raise_amount(1.05)
	print(emp1.raise_amount)

	emp_str_1 = "Asha-K-1000"
	emp2 = Employee.from_string(emp_str_1)
	print(emp2.__dict__)

	from datetime import date
	my_date = date(2017, 6, 7)
	print(Employee.is_workday(my_date))

	print(repr(emp1))
	print(str(emp1))
	print()

	print(1+2)
	print("a"+"b")
	print(int.__add__(1,2))
	print(str.__add__("a","b"))
	print(emp1 + emp2)  # dunder method __add__
	print(len(emp1))  # dunder method __len__

	emp1.lname = "Naik"
	print(emp1.fullname)
	print(emp1.email)
	emp1.fullname = "Nootana D"
	print(emp1.fullname)
	print(emp1.email)
	del emp1.fullname
	print(emp1.fullname)
	print(emp1.email)

if __name__ == "__main__":
	main()
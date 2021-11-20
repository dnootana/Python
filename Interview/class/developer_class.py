#!/usr/bin/env python3.8

from employee_class import Employee

class Developer(Employee):
	raise_amount = 1.10
	def __init__(self, fname, lname, pay, prog_lang):
		super().__init__(fname, lname, pay)
		# Employee.__init__(self, fname, lname, pay)
		self.prog_lang = prog_lang


def main():
	dev1 = Developer("Kavya", "Komal", 2000, "Python")
	dev2 = Developer("Shravya", "Shetty", 1500, "C++")

	print(dev1.__dict__)
	print(dev2.__dict__)

	# print(help(Developer))

	print(dev1.salary)
	dev1.apply_raise()
	print(dev1.salary)

if __name__ == "__main__":
	main()
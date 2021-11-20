import unittest
import sys
from unittest.mock import patch

sys.path.append("../Interview/class/")
# print(sys.path)

from employee_class import Employee

class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("setUpClass")

	@classmethod
	def tearDownClass(cls):
		print("tearDownClass")

	def setUp(self):
		print("setUp")
		self.emp1 = Employee('Nootana', 'Naik', 10000)
		self.emp2 = Employee('Harini', 'Ko', 20000)

	def tearDown(self):
		print("tearDown")

	def test_email(self):
		print("test_email")
		self.assertEqual(self.emp1.email, "Nootana.Naik@company.com")
		self.assertEqual(self.emp2.email, "Harini.Ko@company.com")

		self.emp1.lname = "D"
		self.emp2.lname = "L"

		self.assertEqual(self.emp1.email, "Nootana.D@company.com")
		self.assertEqual(self.emp2.email, "Harini.L@company.com")

		self.emp1.fname = "Jasmin"
		self.emp2.fname = "Gaja"

		self.assertEqual(self.emp1.email, "Jasmin.D@company.com")
		self.assertEqual(self.emp2.email, "Gaja.L@company.com")

	def test_fullname(self):
		print("test_fullname")
		self.assertEqual(self.emp1.fullname, "Nootana Naik")
		self.assertEqual(self.emp2.fullname, "Harini Ko")

		self.emp1.lname = "D"
		self.emp2.lname = "L"

		self.assertEqual(self.emp1.fullname, "Nootana D")
		self.assertEqual(self.emp2.fullname, "Harini L")

		self.emp1.fname = "Jasmin"
		self.emp2.fname = "Gaja"

		self.assertEqual(self.emp1.fullname, "Jasmin D")
		self.assertEqual(self.emp2.fullname, "Gaja L")

	def test_apply_raise(self):
		print("test_apply_raise")
		self.emp1.apply_raise()
		self.emp2.apply_raise()

		self.assertEqual(self.emp1.salary, 11000)
		self.assertEqual(self.emp2.salary, 22000)

	def test_monthly_schedule(self):
		with patch('employee_class.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = "Success"

			schedule = self.emp1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Naik/May')
			self.assertEqual(schedule, "Success")

			mocked_get.return_value.ok = False
			
			schedule = self.emp2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Ko/June')
			self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
	unittest.main()

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        self.my_employee = Employee("Dennis", "Irorere", 10000)
        self.response = 'Dennis Irorere'
        self.salary = 10000
    
    def test_name(self):
        """Test a single resposne store properly."""
        self.assertEqual(self.my_employee.get_employee_name(), self.response)
    
    def test_salary(self):
        """Test the salary"""
        self.assertEqual(self.my_employee.get_salary(), self.salary)    
        
if __name__ == '__main__':
    unittest.main()
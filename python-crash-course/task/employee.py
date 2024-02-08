# class Employee:
#     """user names"""

## Using try and except
print("Employee raise amount")
print("Enter 'q' to quit.")

class Employee:
    """A simple employee compensation scripts"""
    def __init__(self,first, last, salary):
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary
        
    def get_employee_name(self):
        """Return employees name"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name
    
    def get_salary(self):
        """Return salary"""
        salary = self.annual_salary
        return salary
    
    def give_raise(self, raises):
        """Add the given amount to the annual salary"""
        self.annual_salary += raises
        print(f"5,000 annual increase")

employees = Employee("Dennis", "Irorere", 5000)
print(employees.get_employee_name())
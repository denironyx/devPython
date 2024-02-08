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
    
    def give_raise(self, raise_amount=5000):
        """Add the given amount to the annual salary (default: $5,000)"""
        self.annual_salary += raise_amount
        print(f"{raise_amount} annual increase")

employees = Employee("Dennis", "Irorere", 10000)
raise_ = employees.give_raise()
print(f"Name of employee: {employees.get_employee_name()} & Salary: {employees.get_salary()} Next year: {raise_}")


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
        return self.annual_salary

# # Create an instance of Employee
# employee = Employee("Dennis", "Irorere", 10000)

# # Print the initial employee details
# print(f"Name of employee: {employee.get_employee_name()} & Salary: {employee.get_salary()}")

# # Give a raise using the default amount
# next_year_salary = employee.give_raise()
# print(f"Name of employee: {employee.get_employee_name()} & Salary: {employee.get_salary()} Next year: {next_year_salary}")

# # Give a raise with a custom amount
# custom_raise_amount = 7000
# next_year_salary = employee.give_raise(custom_raise_amount)
# print(f"Name of employee: {employee.get_employee_name()} & Salary: {employee.get_salary()} Next year: {next_year_salary}")

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        self.my_employee = Employee("Dennis", "Irorere", 10000)
        self.first = ['Dennis']
    
    def test_response(self):
        """Test a single resposne store properly."""
        self.my_employee.get_employee_name(self.first, self.last)
        self.assertIn(self.response[0], self.my_employee.get_employee_name)

# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey"""
    
#     def setUp(self):
#         """Create a survey and a set of responses for use in all test methods."""
#         question = "What language did you first learn to speak?"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']
    
#     def test_store_single_response(self):
#         """Test that a single response is store properly."""
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)

#     def test_store_three_responses(self):
#         """Test that three individual responses are stored properly."""
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for response in self.responses:
#             self.assertIn(response, self.my_survey.responses)
        
if __name__ == '__main__':
    unittest.main()
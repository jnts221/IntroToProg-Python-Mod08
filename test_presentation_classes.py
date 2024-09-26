# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# Sohail Nassiri,09.25.2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['John', 'Doe', '2024-08-22', 4]):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'John')
            self.assertEqual(self.employee_data[0].last_name, 'Doe')
            self.assertEqual(self.employee_data[0].review_date, '2024-08-22')
            self.assertEqual(self.employee_data[0].review_rating, 4)

        # Simulate invalid review date (not in iso format)
        with patch('builtins.input', side_effect=['Alice', 'Smith', 'invalid date']):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

        # Simulate invalid review rating (not an int)
        with patch('builtins.input', side_effect=['Alice', 'Smith', '2024-08-22', 'invalid rating']):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()
